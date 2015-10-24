import math
import Adafruit_CharLCD as LCD
import time
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
host = socket.gethostname() # Get local machine name
port = 1234               # Reserve a port for your service.
s.bind((host,port))        # Bind to the port
print "SERVER STARTED...."
s.listen(5)                 # Now wait for client connection.
new_s, addr=s.accept()     # Establish connection with client.
print 'Got connection from client'
# Raspberry Pi pin configuration:
lcd_rs        = 7
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,lcd_columns, lcd_rows)

# Print a two line message
string = new_s.recv(200)
print 'CLIENT : ',string
me = "GOT THE STRING ...."
new_s.sendall(me)
s.close()
new_s.close()
length = len(string)
while True:
        lcd.set_cursor(0,0)
        j = 1
        for i in range(0,length):
                k = -1*j
                lcd.message(string[k:])
                time.sleep(0.5)
                j+=1
                lcd.clear()
                lcd.set_cursor(0,0)
        for i in range(1,16-length):
                lcd.set_cursor(i,0)
                lcd.message(string)
                time.sleep(0.5)
                lcd.clear()
        a=1
        q = 16-length
        for i in range(0,length):
                lcd.set_cursor(q,0)
                k = -1*a
                lcd.message(string[:k])
                time.sleep(0.5)
                a+=1
                lcd.clear()
                q+=1

