#Using requests http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
#http://ec2-35-167-227-237.us-west-2.compute.amazonaws.com:1313/beta/add DEV service
#http://ec2-35-163-194-130.us-west-2.compute.amazonaws.com:1313/beta/add QA service
#http://ec2-34-209-188-172.us-west-2.compute.amazonaws.com:1313/beta/add Production

import requests
import json

user_type = "user"
url = "http://ec2-35-163-194-130.us-west-2.compute.amazonaws.com:1313/beta/add"#URL TO ADD A USER
email_list = []

email_responses = open("email_errors.csv", 'a+')
user_list = open("testlist.csv", "r")

#get emails from file and put in email_list[]
for line in user_list:
    email = line.split(',')[0]#getting first element of row
    email_list.append(email)
user_list.close()

#sending email and type to endpoint
for email in email_list[1:]:
    payload = {'email': email, 'type': 'User'}#specifying email and type to add
    r = requests.post(url, payload)#sending payload to URL
    email_responses.write(r.text +",\r\n")#Gathering errors

email_responses.close()

# r = requests.get(url)
# print(json.loads(r.text))
# print(payload)
