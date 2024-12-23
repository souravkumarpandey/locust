from locust import User, task, between


class MyUser(User):

    wait_time = between(1,2)

    # @task
    # def login_URL(self):
    #     print("I am logging into URL")
    #
    # @task
    # def doingwork(self):
    #     print("I am doing my work")
    #
    # @task
    # def logingout(self):
    #     print("I am logging out")

    def on_start(self):
        print("I am logging into URL")

    @task
    def doingwork(self):
        print("I am doing my work")

    def on_stop(self):
        print("I am logging out")
