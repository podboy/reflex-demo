import reflex as rx


def Footer() -> rx.Component:
    """A footer component"""
    return rx.vstack(
        rx.divider(size="4"),
        rx.hstack(
            rx.link(
                rx.text("Made with ❤️ by Reflex"),
                href="https://reflex.dev",
                target="_blank",
            ),
            justify="center",
            width="100%",
        ),
        width="100%",
    )
