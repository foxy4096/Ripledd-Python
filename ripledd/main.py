import hashlib

import requests

from . import constants

client = requests.Session()


class Ripledd:
    """
    A nice and sweet API wrapper made for [Ripledd](https://ripledd.com/center/)
    """

    API_URL: str = constants.API_URL
    ENDPOINTS = {
        "create_post": "post.php",
    }

    def __init__(self, email: str, password: str) -> None:
        self.email: str = email
        self.password: str = hashlib.sha256(password.encode("utf-8")).hexdigest()

    def create_post(self, body) -> requests.Response:
        """
        Creating a Post
        """
        body = {
            "spchr_auth_email": self.email,
            "spchr_auth_pw_hash": self.password,
            "send_data": body,
        }
        res = client.post(
            url=f"{self.API_URL}{self.ENDPOINTS.get('create_post')}", data=body
        )
        return res


