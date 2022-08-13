
from locust import HttpUser, between, task
import uuid
import json



class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    @task
    def on_start(self):
        self.client.headers ={
                "sec-ch-ua-platform": "\"macOS\"",
                "Referer": "http://localhost:4200/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            }
    # def on_start(self):
    #     self.client.get("/")

    # @task
    # def welcome(self):
    #     self.client.get("/petclinic/welcome")

    @task
    def owners(self):
        self.client.get("/petclinic/api/owners")
    
    @task
    def vets(self):
        self.client.get("/petclinic/api/vets")

    @task
    def add_vets(self):
        self.client.post("/petclinic/api/vets", data=json.dumps({
            "id": "null",
            "firstName": "Vishal",
            "lastName": "Mishra",
            "specialties": [
                {
                "id": 3,
                "name": "dentistry"
                }
            ]
            }),
                headers={
                "accept": "application/json, text/plain, */*",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "content-type": "application/json",
                "elastic-apm-traceparent": "00-06f0a3172fab4183432abaed1d5266eb-76c98944a841757d-01",
                "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"macOS\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "Referer": "http://localhost:4200/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
  
            })


    @task
    def pettypes(self):
        self.client.get("/petclinic/api/pettypes")

    @task  
    def specialties(self):
        self.client.get("/petclinic/api/specialties")
