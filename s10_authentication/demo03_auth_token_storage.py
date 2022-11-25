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

    def list_git_hub_repositories():
        lvw_repositorios.controls.clear()
        if page.auth:
            headers = {
                'Authorization': 'Bearer {}'.format(page.auth.token.access_token)
            }

            response = requests.get(
                'https://api.github.com/user/repos',
                headers=headers
            )

            repositorios = json.loads(response.text)

            for r in repositorios:
                lvw_repositorios.controls.append(
                    ListTile(
                        leading=Icon(icons.FOLDER_ROUNDED),
                        title=Text(r['fullname'])
                    )
                )

    def logout_click(event):
        page.client_storage.remove(AUTH_TOKEN_KEY)
        page.logout()
    
    def on_logout(event):
        toggle_login_buttons()
        list_git_hub_repositories
        page.update()
    
    def toggle_login_buttons():
        btn_login.visible = page.auth is None
        lbl_user.visible = btn_logout.visible = page.auth is not None
    
    
    