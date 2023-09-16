""" Import module.
We need the data in the form of a list of lists. The 0th index of the outer index is the headers.
We create a simple doc template with the specified paper size (here A4)
Then get a sample style sheet from the built-in style sheets and add the styling accordingly.
After you have created a style object, feed in the data and the style sheet to the pdf object and build it.
"""

# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# data which we are going to display as tables
DATA = [
	[ "Date" , "Name", "Subscription", "Price (Rs.)" ],
	[
		"16/11/2020",
		"Frontend Development: Html, Css, Javascript, React",
		"15 Weeks",
		"75,000.00/-",
	],
	[ "16/11/2020", "Backend Development: Python, Django", "10 Weeks", "50,000.00/-"],
	[ "Total", "", "", "125,000.00/-"],
]

# creating a Base Document Template of page size A4
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )

# standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

# fetching the style of Top level heading (Heading1)
title_style = styles[ "Heading1" ]

# 0: left, 1: center, 2: right
title_style.alignment = 1

# creating the paragraph with
# the heading text and passing the styles of it
title = Paragraph( "Zindua School" , title_style )

# creates a Table Style object and in it,
# defines the styles row wise
# the tuples which look like coordinates
# are nothing but rows and columns
style = TableStyle(
	[
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
		( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
	]
)

# creates a table object and passes the style to it
table = Table( DATA , style = style )

# final step which builds the
# actual pdf putting together all the elements
pdf.build([ title , table ])
