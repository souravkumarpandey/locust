import re

from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)

    host = "https://www.geeksforgeeks.org/"

    @task
    def login_URL(self):
       res= self.client.get("/geeksforgeeks-practice-best-online-coding-platform/?ref=ghm",name="practice page")

       res1=re.findall("Write and publish your .*",res.text)
       print(res1)