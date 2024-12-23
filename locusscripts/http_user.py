from locust import HttpUser, task, between


class MyUser(HttpUser):

    wait_time = between(1,2)
    host="http://newtours.demoaut.com/"
    @task
    def login_URL(self):
        print("I am logging into URL")



#running from the command line
#locust -f basic_http_host.py --host="http://newtours.demoaut.com/"