from reactpy import component, run, web,html
from fastapi import FastAPI
from reactpy.backend.fastapi import configure

mui = web.module_from_template(
    "react",
    "@mui/material",
    fallback="waiting for my component .....",
)

Button = web.export(mui, "Button")
Card = web.export(mui, "Card")
CardContent = web.export(mui, "CardContent")
CardActions = web.export(mui, "CardActions")
Typography = web.export(mui, "Typography")
Alert = web.export(mui, "Alert")
app = FastAPI()

@component
def HelloWorld():
    return html.div(
        Button({"color": "primary", "variant": "contained"}, "Hello World!"),
        Card({
            "margin":"20px"
            },
            CardContent(
                Typography({
                    "variant":"h2"
                },"hello word Reactpy") 
                ),
            CardActions(
        Button({"color": "primary", "variant": "contained"}, "Hello World!"),

                )
        ),
        Alert({
            "severity":"success"
            },
            "this alert test"
            )

        )


configure(app,HelloWorld)