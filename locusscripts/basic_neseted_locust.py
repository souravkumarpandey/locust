
from locust import User, task, between, TaskSet, SequentialTaskSet


class UserBehavior(TaskSet ):
    @task
    class CartModule(TaskSet):
        @task()
        def add_cart(userclass):
            print("I am add to cart")
    @task()
    def delete_cart(userclass):
        print("i am delete cart")
    @task
    class Product_Module(TaskSet):
        @task()
        def view_product(userclass):
            print("I am view product")

        @task()
        def view_product(userclass):
            print("I  add product")

class MyUser(User):
    wait_time = between(1,2)
    tasks=[UserBehavior]