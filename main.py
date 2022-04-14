import mysql.connector
import time

import serial
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="laravel_user",
    passwd="qwerty",
    database="communication"
)
mycursor = mydb.cursor()

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)

while True:
    mycursor.execute("SELECT * FROM led;")
    for x in mycursor:
        print(x[1])
    
    if(x[1] == 'aan'):
        # print(x[1])
        port.write(b"l1")

    else:
        port.write(b"l0")



    rcv = port.readline().strip()
    if (b'b' in rcv):
        print("Pressed the button -> +1")
        os.system("python update.py")

    time.sleep(1)
    mydb.commit()

mydb.close()