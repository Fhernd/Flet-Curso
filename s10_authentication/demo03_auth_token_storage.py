import json
import os

import flet
import requests
from flet import (
    AppBar,
    ElevatedButton,
    Icon,
    ListTile,
    ListView,
    LoginEvent,
    Page,
    Row,
    Text,
    icons
)
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from flet.security import decrypt, encrypt


def main(page: Page):
    secret_key = os.getenv('MY_APP_SECRET_KEY')

    provider = GitHubOAuthProvider(
        client_id=os.getenv('GITHUB_CLIENT_ID'),
        client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
        redirect_url='http://localhost:8550/api/oauth/redirect'
    )

    AUTH_TOKEN_KEY = 'myapp.auth_token'

    
