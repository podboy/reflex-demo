import reflex as rx


@rx.page(route="/device")
def device() -> rx.Component:
    return rx.vstack(
        rx.mobile_only(
            rx.text("📱 Mobile view"),
        ),
        rx.tablet_only(
            rx.text("📱 Tablet view"),
        ),
        rx.desktop_only(
            rx.text("💻 Desktop view"),
        ),
        rx.mobile_and_tablet(
            rx.text("Visible on Mobile and Tablet"),
        ),
        rx.tablet_and_desktop(
            rx.text("Visible on Desktop and Tablet"),
        ),
        rx.link(
            rx.button("Back to Home"),
            href="/",
            is_external=False,
        ),
        width=["100%", "80%", "60%"],   # mobile / tablet / desktop
        padding=["1em", "2em", "4em"],
        spacing="3",
    )
