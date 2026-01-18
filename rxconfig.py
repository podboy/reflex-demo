import reflex as rx

config = rx.Config(
    app_name="webapp",
    app_module_import="myapp.app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
