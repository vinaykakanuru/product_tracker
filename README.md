# Django App demonstrating Zappa deployment

![Python 3.7.3](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![Django 3.1.7](https://img.shields.io/badge/Django-3.1.7-skyblue.svg) ![zappa 0.52.0](https://img.shields.io/badge/zappa-0.52.0-skyblue.svg)

• A simple and basic Web application to upload files to **_AWS S3_** and access the files using **_S3 URL_**.

• It helps you in deploying Django Application to **_AWS Lambda_** using **_zappa_** library.

• You need to create an account in **_http://console.aws.amazon.com_** in order to access AWS.

• Create a **_IAM user_** through AWS Console and add **_IAM Full Access_** permission and create a new policy with **_AWS text file_** and attach to the user.

• Configure AWS **_ACCESS_KEY_ID_**, **_AWS_SECRET_ACCESS_KEY_** in AWS configuration file using **_AWS CLI_**.

• Use the following commands

```sh
$ pip install zappa
$ zappa init
$ zappa deploy <envt>
```

• If you see the below error then  
Error: Warning! Status check on the deployed lambda failed. A GET request to '/' yielded a 500 response code.
(Sometimes you can find SQLITE version issue. Use compatible Version or you can go with AWS RDS for DB)

```sh
$ zappa tail
```

• The above command shows the error logs to analyze the issues. After solving the issue please update the deployment using below command.

```sh
$ zappa update <envt>
```

• You can find the live URL for your web app once update is done.
![zappa-update](readme_resources/updatecmd.JPG)

• Please do ⭐ the repository, if it helped you in anyway.
