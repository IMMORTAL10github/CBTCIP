
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Table,Paragraph,TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
grocery_items = [
    ["grocery","count","price(in Rs)"],
    ["apple", "2", "50"],
    ["banana", "3", "30"],
    ["carrot", "1", "15"],
    ["bread", "2", "15"],
    ["milk", "2", "20"],
    ["Total","","130"]
]
pdf=SimpleDocTemplate("grocery_receipt.pdf",pagesize=A4)
styles=getSampleStyleSheet()
title_style=styles["Heading1"]
title_style.alignment=1
title=Paragraph( "grocery list" , title_style)
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 5 , 5 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.yellow ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.green ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
)
grocery_table=Table(grocery_items,style=style)
pdf.build([title,grocery_table])