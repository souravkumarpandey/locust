from locust import  User, task,between


def add_cart(s):
    print("I am add to cart")

def view_product(self):
        print("I am viewing product")

class MyUser(User):
    wait_time = between(1,2)

    # tasks=[add_cart,view_product]
    tasks={add_cart:10,view_product:1}
