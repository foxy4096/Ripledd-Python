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

    def __init__(self, email: str, password: str, channel_id = None) -> None:
        self.email: str = email
        self.password: str = password
        self.channel_id: str = channel_id

    def create_post(self, body) -> requests.Response:
        """
        Creating a Post
        """
        body = {
            "email": self.email,
            "password": self.password,
            "content": body,
            "channel_id": self.channel_id
        }
        return client.post(
            url=f"{self.API_URL}{self.ENDPOINTS.get('create_post')}", data=body
        )


