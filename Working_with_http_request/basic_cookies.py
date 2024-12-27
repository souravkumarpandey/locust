from locust import HttpUser, SequentialTaskSet, task, between

class UserBehavior(SequentialTaskSet):
    @task
    def print_cookies(self):
        response = self.client.get("https://www.geeksforgeeks.org/geeksforgeeks-practice-best-online-coding-platform/?ref=ghm")
        cookies = response.cookies
        for cookie in cookies.items():
            print(f"Cookie Name: {cookie[0]}, Cookie Value: {cookie[1]}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 9)
    host = "https://www.geeksforgeeks.org"
