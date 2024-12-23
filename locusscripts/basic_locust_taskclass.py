from locust import  User, task,between, TaskSet

class UserBehavior(TaskSet):
    @task
    def add_cart(s):
        print("I am add to cart")
    @task
    def view_product(self):
        print("I am viewing product")

class MyUser(User):
    wait_time = between(1,2)
    tasks=[UserBehavior]




class MyUser(User):
    wait_time = between(1,2)
    @task
    class UserBehavior(TaskSet):
        @task
        def add_cart(s):
            print("I am add to cart")

        @task
        def view_product(self):
            print("I am viewing product")