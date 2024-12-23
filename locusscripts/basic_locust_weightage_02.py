from locust import User, task, between


class MyWebUser(User):

    wait_time = between(1,2)
    weight = 3
    @task
    def login_URL(self):
        print("I am web")

class MyMobileUser(User):

    wait_time = between(1,2)
    weight = 1
    @task
    def login_URL(self):
        print("I am mobile")

# locust -f .\basic_locust_weightage_02.py MyWebUser

#weight is likly hood
# --headless
#-u ,--user
#-r, --hatch-rate
#-t ,--run-time
#--logfile

# locust -f .\basic_locust_weightage_02.py MyWebUser -u 5 -r 1 -t 60s --headless --logfile mylog/mylog


