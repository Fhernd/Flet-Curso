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

    def login(event):
        saved_token = None

        token = page.client_storage.get(AUTH_TOKEN_KEY)

        if token:
            saved_token = decrypt(token, secret_key)
        
        if event is not None or saved_token is not None:
            page.login(provider, saved_token=saved_token, scope=['public_repo'])
    
    def on_login(event: LoginEvent):
        if event.error:
            raise Exception(event.error)
        
        token = page.auth.token.to_json()
        token_encriptado = encrypt(token, secret_key)
        page.client_storage.set(AUTH_TOKEN_KEY, token_encriptado)

        lbl_user.value = f"¡Hola, {page.auth.user['name']}!"
        toggle_login_buttons()
        list_git_hub_repositories()
        page.update()

    
