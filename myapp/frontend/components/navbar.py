import reflex as rx


def Navbar() -> rx.Component:
    """A navbar component"""
    return rx.vstack(
        rx.hstack(
        ),
        rx.divider(size="4"),
        width="100%",
    )
