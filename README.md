# serverless

> A lambda function that has email sending and anti-duplication implemented. The intent is to sever for [webapp](https://github.com/gaoxiaob-fall2020/webapp.git) by triggering the function on answer updates, as a result of which whenever there is a new answer, updated answer, or deleted answer to a question, the question's creator will get an email notification. 

## Run in Local Development

**> *Install Python3.6+, virtualenv***

**> *Configure local AWS profile***
* Install AWS Command Line Interface
  * [AWS CLI Installations](https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html)
  <br>
* Generate access keys from [My Security Credentials](https://console.aws.amazon.com/iam/home?region=us-east-1#/security_credentials). IAM users should have Programmatic access to DynamoDB.
  <br>
* Configure local AWS profile
  * <code>$ aws configure --profile profile-name</code>
  * Enter access keys and region as prompted 

**> *Set environment variable***
    
    export DYNANODB_TABLE=x   # Name of dynamodb table that keeps track of sent emails for auti-duplication.

**> *Run the function***

    $ cd <repo-root>
    $ virtualenv python env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python
    >>> from lambda_function import lambda_handler


## Build and Deploy instructions for webapp

The function is intent to server for webapp and expect to receive messages from SNS that have been published by webapp. Below are properties that must included in a message body:

    'on':string, from 'question_answered', 'answer_updated', and 'answer_deleted' 
    'question_id': string, id of a question that has an answer update   
    'question_creator_email': email of a question's creator
    'question_text': string, content of a question that has an answer update
    'question_url': string, url of a question that has an answer update
    'answer_id': string, id of an answer
    'answer_text': string, content of an answer
    'answer_url': string, url of an answer, which can be ignored on answer_deleted 