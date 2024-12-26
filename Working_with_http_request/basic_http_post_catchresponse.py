from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)

    host = "https://www.javatpoint.com/"

    @task
    def login_URL(self):
        with self.client.get("simple-html-pages",catch_response=True) as resp:
            # print(resp)
            if("Learn Important Tutorial")in resp.text:
                resp.success()
            else:
                resp.failure("failed to launch url")
        # print(res.text)
        # print(res.status_code)
        # print(res.headers)
