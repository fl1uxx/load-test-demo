from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def index(self):
        self.client.get("/")

    @task(2)
    def users(self):
        self.client.get("/users")

    @task(1)
    def health(self):
        self.client.get("/health")