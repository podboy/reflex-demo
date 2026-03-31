import reflex as rx
from reflex_xpw_backend import LogoutState
from reflex_xpw_defender import Defender
from reflex_xpw_settings import CONFIG


@rx.page(route="/account")
@Defender.login_required
def account() -> rx.Component:
    return rx.vstack(
        rx.text("Demo Account"),
        rx.link(
            rx.button("Back to Home"),
            href="/",
            is_external=False,
        ),
        rx.link(
            rx.button("Goto Logout"),
            href=CONFIG.routes.logout,
            is_external=False,
        ),
        rx.button("Logout", on_click=LogoutState.on_submit),
        width=["100%", "80%", "60%"],   # mobile / tablet / desktop
        padding=["1em", "2em", "4em"],
    )
