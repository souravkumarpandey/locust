
from locust import User, task, between, TaskSet, SequentialTaskSet


class UserBehavior(SequentialTaskSet ):
    @task
    def flight_finder(s):
        print("i will find flight by entering criteria")
    @task
    def select_flight(self):
        print("select flight")

    @task
    def book_flight(self):
        print("book_flight")

class MyUser(User):
    wait_time = between(1,2)
    tasks=[UserBehavior]