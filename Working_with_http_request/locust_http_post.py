from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)

    host = "https://api.escuelajs.co/api/v1/auth/"

    # @task
    # def login_URL(self):
    #     self.client.get("/geeksforgeeks-practice-best-online-coding-platform/?ref=ghm",name="practice page")

    @task
    def login(self):
     response=self.client.post("login",data={
  "email": "john@mail.com",
  "password": "changeme"
})
     print(response.text)
