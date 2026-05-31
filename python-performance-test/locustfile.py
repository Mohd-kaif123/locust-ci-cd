from locust import HttpUser, task, between

class MyStressTestUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_posts_users(self):
        self.client.get("/health")
    @task
    def get_posts_users(self):
        self.client.get("/")
        
      