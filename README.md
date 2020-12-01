# serverless

> A lambda function that has email sending and anti-duplication implemented. The intent is to sever for [webapp](https://github.com/gaoxiaob-fall2020/webapp.git) by triggering the function on answer updates, as a result of which whenever there is a new answer, updated answer, or deleted answer to a question, the question's creator will get an email notification. 

## Run in Local Development

**> *Install Python3.6+, virtualenv***

**> *Configure local AWS profile***
* Install AWS Command Line Interface
  * [AWS CLI Installations](https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html)
  <br>
* Generate access keys from [My Security Credentials](https://console.aws.amazon.com/iam/home?region=us-east-1#/security_credentials). IAM users should have Programmatic access of AmazonVPCFullAccess.
  <br>
* Configure local AWS profile
  * <code>$ aws configure --profile profile-name</code>
  * Enter access keys and region as prompted 

**> *Set environment variables(use <code>export TF_VAR_<var_below></code> command on Linux/Unix)***
* <code>profile</code> String. Name of local AWS Authenticated profile
* <code>region</code> String. Region associated with the profile
* <code>account_id</code> String. AWS account ID
* <code>vpc_cidr</code> String. CIDR block for the VPC
* <code>subs_cidr</code> Map. CIDR blocks for subnets
* <code>ava_zones</code> Map. Availability zones under the region. map keys must be consistent with those of subs_cidr
* <code>public_key_path</code> String. Path of your ssh public key
* <code>ssh_key_name</code> String. Name of the ssh public key
* <code>ami</code> String. AMI id upon which an EC2 instance will be created for testing
* <code>instance_type</code> String. EC2 instance type
* <code>sub_id</code> String. Subnet id where the EC2 instance get launched
* <code>b_name</code> String. S3 bucket name
* <code>db_identifier</code> String. RDS database identifier
* <code>db_name</code> String. RDS database name
* <code>db_uname</code> String. RDS master username
* <code>db_pwd</code> String. RDS master password
* <code>db_subs_name</code> String. Name of subnet group for the database instance
* <code>dynamodb_tbl_name</code> String. Dynamodb table name
* <code>iam_p_name</code> String. Name of IAM police
* <code>iam_r_name</code> String. Name of IAM role
* <code>gh_cd_uname</code> String. IAM user name for github actions to perform CD
* <code>codedeploy_app_name</code> String. Name of CodeDeploy application
* <code>codedeploy_b_name</code> String. Bucket name for webapp artifacts
* <code>hosted_zone_id</code> String. Public hosted zone id
* <code>api_subdomain_name</code> String. Subdomain name for webapp

**> *Create a VPC and its rescources***

    $ cd <repo-root>
    $ terraform init
    $ terraform validate    # proceed if no errors found
    $ terraform apply  

**> *Destroy a previous VPC and its rescources***
    
    $ cd <repo-root>
    $ terraform destroy
    
