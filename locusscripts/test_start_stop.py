
from locust import User, task, between,events


@events.test_start.add_listener
def script_start(**kwargs):
    print("i am connecting to DB")

@events.test_stop.add_listener
def script_stop(**kwargs):
    print("i am disconnecting from DB")


class MyUser(User):

    wait_time = between(1,2)



    def on_start(self):
        print("I am logging into URL")

    @task
    def doingwork(self):
        print("I am doing my work")

    def on_stop(self):
        print("I am logging out")
