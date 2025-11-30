from api.api_calls.auth_token import AuthTokenCalls
from logging import getLogger

logger = getLogger(__name__)

class AuthTokenImpl:

    username = "admin"
    password = "password123"

    def __init__(self):
        self.auth_token_calls = AuthTokenCalls(self.username, self.password)

    def generate_auth_token_for_apis(self):
        """
        :return: Parameter of auth_token and API response status
        """

        status = False
        auth_token = ""

        try:
            logger.info("Getting new auth token for API usage")
            response = self.auth_token_calls.post_api_auth_token_call()
            if response.ok:
                status = True
                auth_token = response.json()["token"]

        except Exception as e:
            logger.error(f"Error in calling create auth token API with: {e}")

        return auth_token, status
