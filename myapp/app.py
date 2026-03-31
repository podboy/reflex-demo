"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_xpw_frontend import LoginPage
from reflex_xpw_frontend import LogoutPage

from .backend.api import fastapi_app
from .frontend.pages import *

app = rx.App(api_transformer=[fastapi_app])

LoginPage().mount(app)
LogoutPage().mount(app)
