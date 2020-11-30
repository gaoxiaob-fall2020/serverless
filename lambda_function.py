import json
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3
import os

SMTP_SERVER='email-smtp.us-east-1.amazonaws.com'
SMTP_PORT=587
SMTP_UNAME='AKIAYNXSWQLYBDQDZS4G'
SMTP_PWD='BKfPM0UCw4WwMPOTPnuc310SpcQdCbCopV5h5IcrpOZr'
DYNANODB_TABLE=os.environ['DYNANODB_TABLE']

def _send_email(fro, to, subject, content, html=False):
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SMTP_UNAME, SMTP_PWD)

        msg = MIMEMultipart()
        msg['From'] = fro
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(content + '\n\n\n')
                   ) if not html else msg.attach(MIMEText(content + '<br><br><br>', 'html'))

        server.sendmail(fro, to, str(msg))

def lambda_handler(event, context):
    message_id = event['Records'][0]['Sns']['MessageId']
    message = json.loads(event['Records'][0]['Sns']['Message'])
        
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNANODB_TABLE)
    item = table.get_item(
        Key={
            'id': message_id
        }
    )
    if item:
        return {
        'statusCode': 400,
        'body': json.dumps('Message has already been sent.')
        }
        
    _send_email('webapp <notifications@xiaobingao.me>', 'gao.xiaob.dev@outlook.com', message_id, msg)
    # for i in event:
    #     print(i)
    # TODO implement
    table.put_item(
        Item={
            'id': message_id,
            'on': message.get('on'),
            'question_id': message.get('question_id'),
            'question_creator_email': message.get('question_creator_email'),
            'question_url': message.get('question_url'),
            'answer_id': message.get('answer_id'),
            'answer_text': message.get('answer_text'),
            'answer_url': message.get('answer_url')
        }    
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
