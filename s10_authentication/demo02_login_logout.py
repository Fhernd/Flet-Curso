import os

import flet
from flet import ElevatedButton, LoginEvent, Page
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider


def main(page: Page):
    provider = GitHubOAuthProvider(
        client_id=os.getenv('GIT_CLIENT_ID'),
        client_secret=os.getenv('GIT_CLIENT_SECRET'),
        redirect_url='http://localhost:8550/api/oauth/redirect'
    )

    def login_click(event):
        page.login(provider, scope=['public_repo'])

    def on_login(event: LoginEvent):
        if not event.error:
            toggle_login_buttons()
    
    def logout_click(event):
        page.logout()
    
    def on_logout(event):
        toggle_login_buttons()
    
    def toggle_login_buttons():
        btn_login.visible = page.auth is None
        btn_logout.visible = page.auth is not None

        page.update()

    btn_login = ElevatedButton('Login with GitHub', on_click=login_click)
    btn_logout = ElevatedButton('Logout', on_click=logout_click)
    
    toggle_login_buttons()

    page.on_login = on_login
    page.on_logout = on_logout

    page.add(
        btn_login,
        btn_logout
    )


flet.app(target=main, port=8550, view=flet.WEB_BROWSER)
