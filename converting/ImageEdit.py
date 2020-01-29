import pyodbc
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import XBMConv.converting.Main

conn = pyodbc.connect('''Driver={SQL Server};
                        Server=tcp:localhost,50001;
                        Database=Projekt_Türschild;
                        UID=Python_Connect;
                        PWD=Python;''')

last_Row = None


def insert_into_Image(ImageValue):
    Name = (ImageValue[0].replace(" ", "\n"))
    Raum = (ImageValue[1])
    Datum = (ImageValue[2])

    img = Image.open("../../Converting/image.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("C:\Windows\Fonts\comic.ttf", 40)
    draw.text((30, 85), Name, (0, 125, 125), font=font)
    draw.text((350, 85), Raum, (0, 125, 125), font=font)
    draw.text((10, 285), Datum, (0, 125, 125), font=font)
    img.save("C:/Users/Administrator/Documents/Project_Türschild/XBMConv/converting/image.png")

def Fetch_Last_Row():
    global last_Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Blackboard')
    DB_Data = []
    for row in cursor:
        DB_Data.append(row)

    if last_Row == None:
        last_Row = DB_Data[-1]
        print("Erster Durchlauf")
        print(last_Row)
    elif last_Row == DB_Data[-1]:
        print("Kein neuer Wert")
        print(last_Row)
    else:
        print("Neuer Wert")
        last_Row = DB_Data[-1]
        insert_into_Image(last_Row)
        print(last_Row)


while True:
    time.sleep(3)
    print("Suche nach neuen Werten...")
    Fetch_Last_Row()


