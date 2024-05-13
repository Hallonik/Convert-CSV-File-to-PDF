
from fpdf import FPDF
from fpdf.fonts import FontFace
import csv


#open the csv file
with open (r"C:\Users\user1\Desktop\python files\CSV-To-PDF\Countries.txt",encoding="utf-8") as csv_file:#raw file is imported
    #each item in the list represents a row of the txt file
    #delimiter can be , or : based on how the items
    #are seperated in a row
    data=list(csv.reader(csv_file,delimiter=","))

#create pdf using fpdf
pdf=FPDF()
#set the font
pdf.set_font("helvetica",size=14)

#add page
pdf.add_page()

pdf.set_draw_color(255,0,0)#to set the border cplours

pdf.set_line_width(0.5)
#setting the heading style
headings_style = FontFace(emphasis="BOLD",color=225,fill_color=(225,100,0))
#to create a table
#add styling to the table
with pdf.table(
    borders_layout="NO_HORIZONTAL_LINES",#removes all horizontal lines from table
    cell_fill_color=(224,235,255),#to fill every cell with a colour
    col_widths=(42,39,35,42),#set column widths it uses tuple
    line_height=6,
    headings_style=headings_style,
    text_align=("LEFT","CENTER","RIGHT","RIGHT"),#to align the data of different col.
    width=160,
    

) as tab:
    #to get every single data
    for data_row in data:
        row=tab.row()
        #creating cell for every single data in a row
        for datum in data_row:
            row.cell(datum)

pdf.output("PDFtable.pdf")
    






