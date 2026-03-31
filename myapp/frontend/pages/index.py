import reflex as rx
from reflex_xpw_defender import Defender

from ..layouts.main_layout import main_layout


@rx.page(route="/")
@Defender.no_login_required
def index() -> rx.Component:
    # Welcome Page (Index)
    return main_layout(
        rx.vstack(
            rx.heading("Welcome", size="9"),
            rx.text("This is a demo app."),
            rx.link(
                rx.button("Account"),
                href="/account",
                is_external=False,
            ),
            rx.link(
                rx.button("Device"),
                href="/device",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            # min_height="50vh",
        ),
    )
