import time
from locust import HttpUser, task, between
import json

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_items(self):
        body = {}
        url = '/athu/api/check'
        headers = {'content-type': 'application/json'}
        self.client.post(url, json=body, headers=headers)

