import pyodbc
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import XBMConv.converting.Main as XBMConvert

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

    img = Image.open("Vorlage.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("C:\Windows\Fonts\comic.ttf", 40)
    draw.text((30, 85), Name, (0, 125, 125), font=font)
    draw.text((350, 85), Raum, (0, 125, 125), font=font)
    draw.text((10, 285), Datum, (0, 125, 125), font=font)
    img.save("image.png")

def Fetch_Last_Row():
    global last_Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Blackboard')
    DB_Data = []
    for row in cursor:
        DB_Data.append(row)

    if last_Row == None:
        last_Row = DB_Data[-1]
        print("Ersteraufnahme von Datenbankwerten\n")
        print("Letzter bekannter Wert:" + str(last_Row) + "\n")
    elif last_Row == DB_Data[-1]:
        print("Kein neuer Wert\n")
        print("Letzter bekannter Wert:" + str(last_Row) + "\n")
    else:
        print("Neuer Wert gefunden!\n")
        last_Row = DB_Data[-1]
        insert_into_Image(last_Row)
        print("Letzter bekannter Wert:" + str(last_Row) + "\n")


while True:
    time.sleep(3)
    print("Suche nach neuen Werten...\n")
    Fetch_Last_Row()
    XBMConvert.XBM_Converter()


