### Network Security Projects For Phising Data
The aim of this project is to train an ML model to detect whether the website is legit or not using various parameters. Following steps are performed in this project:
1) Parameter Configuration
2) Data Ingestion
3) Data Validation
4) Data Transforamtion & Feature Engineering
5) Model Training
6) Writing the Dockerfile 
7) Pushing the model to github Repo
8) CI/CD pipeline on Gihub 
9) AWS ECR repo and EC2 instance creation
10) Deploying the model to the cloud

Note: The configuratio of AWS with Github requires proper secret management and the EC2 instance needs some packages to be able to run the model. You can store the credentials in github secrets and use them in your pipeline. For this project you need following secerets and variables configured properly:
Setup github secrets:
AWS_ACCESS_KEY_ID= YOUR_ID

AWS_SECRET_ACCESS_KEY= YOUR_SECRET

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = YOUR_ECR_URI
ECR_REPOSITORY_NAME = YOUR_REPOR_NAME

###Actions to be performed on EC2 instance before deploying the model

Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker