import requests
from utils.configs.url_links import get_base_api_url

class AuthTokenCalls:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post_api_auth_token_call(self):

        api_base_url = get_base_api_url()
        endpoint = "auth"
        headers = {"Content-Type": "application/json"}
        json_body = {"username" : self.username, "password" : self.password}


        response = requests.post(f"{api_base_url}/{endpoint}", headers=headers, json=json_body)

        return response
