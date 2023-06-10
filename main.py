from reactpy import html,run,component,web
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

mui = web.module_from_template(
	"react",
	"@mui/material",
	fallback="please wait loading ...."
	)
# AND NOW I WILL CREATE BUTTON WITH MATERIAL UI
Button = web.export(mui,"Button")
Card = web.export(mui,"Card")
CardContent = web.export(mui,"CardContent")
CardActions = web.export(mui,"CardActions")
Alert = web.export(mui,"Alert")
Typography = web.export(mui,"Typography")





app = FastAPI()
@component
def Myapp():
	return html.div(
		Button({
			"color":"primary",
			"variant":"contained"

			},"my first button"),

		# AND I CREATE CARD
		Card(
			CardContent(
				Typography(
					{
						"variant":"h2",

					},"HELLOW WORLD")
				),
			CardActions(
				Button({
			"color":"primary",
			"variant":"contained"

			},"my SUbmit data"),
				)
			),
		# AND ALERT
		Alert(
			{"severity":"success"},"this alert test")

		)
	
configure(app,Myapp)

