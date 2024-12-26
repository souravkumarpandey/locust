from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)

    host = "https://www.javatpoint.com/"

    @task
    def login_URL(self):
        res=self.client.get("simple-html-pages")
        print(res.text)
        print(res.status_code)
        print(res.headers)
