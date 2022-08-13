from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    @task
    def login(l):
        l.client.get("/")

    @task
    def welcome(l):
        l.client.get("/petclinic/welcome")

    @task
    def owners(l):
        l.client.get("/petclinic/owners")
    
    @task
    def pettypes(l):
        l.client.get("/petclinic/pettypes")
    @task  
    def specialties(l):
        l.client.get("/petclinic/specialties")
