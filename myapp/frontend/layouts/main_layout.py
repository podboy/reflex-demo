import reflex as rx

from ..components.footer import Footer
from ..components.navbar import Navbar


def main_layout(*children: rx.Component) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.tablet_and_desktop(
                rx.color_mode.button(position="top-right"),
            ),
            Navbar(),
            *children,
            rx.spacer(flex_grow=1),
            Footer(),
            height="100%",
            width=["100%", "80%", "60%"],   # mobile / tablet / desktop
            padding=["1em", "2em", "4em"],
        )
    )
