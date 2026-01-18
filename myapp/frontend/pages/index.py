import reflex as rx

from ..layouts.main_layout import main_layout


@rx.page(route="/")
def index() -> rx.Component:
    # Welcome Page (Index)
    return main_layout(
        rx.vstack(
            rx.heading("Welcome", size="9"),
            rx.text("This is a demo app."),
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
