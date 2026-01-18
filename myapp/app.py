"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .backend.api import fastapi_app
from .frontend.pages import *

app = rx.App(api_transformer=[fastapi_app])
