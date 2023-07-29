# 
# 
# http://skpang.co.uk/catalog/pican2-canbus-board-for-raspberry-pi-2-p-1475.html
#
# Make sure Python-CAN is installed first http://skpang.co.uk/blog/archives/1220
#
# Uses PiCan3 CAN board
# Uses HDMI Waveshare 7.9" LCD 1280 x 400
#
# Note: To rotate screen do NOT use config.txt, use pi menu function
# Note: To rotate the touch Screen use the button on the back of the LCD panel
#
# Note Vent fan icon does NOT follow actual state, only if this LCD opens or closes the vents.
#       Rear Bath room lights & Halfbath lightes are controlled together. LCD icon follows the vanity light
#
#
#
import tkinter
from tkinter import *
 
master=tkinter.Tk()
master.title("grid() method")
master.geometry("1280x400")
#master.attributes('-fullscreen', True)
#master.config(cursor="none")

import RPi.GPIO as GPIO
import can
import time
import os
import queue
from threading import Thread
led = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)
os.system("sudo /sbin/ip link set can0 down")
print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can0 up type can bitrate 250000")

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
except OSError:
    print('Cannot find PiCAN board.')
    GPIO.output(led,False)
    exit()

bus.set_filters([{"can_id": 0x19FEDA8E, "can_mask": 0xFFFF00, "extended": True}])

B_state_1 = 3
B_state_2 = 3
B_state_3 = 3
B_state_4 = 3
B_state_5 = 3
B_state_6 = 3
B_state_7 = 3
B_state_8 = 3
B_state_9 = 3
B_state_10 = 3
B_state_11 = 3
B_state_12 = 3
B_state_13 = 3
B_state_14 = 3

photo_1 = PhotoImage(file = 'Bedroom_Light_Off.png')
photo_1_On = PhotoImage(file = 'Bedroom_Light_On.png')

photo_5 = PhotoImage(file = 'All_Lights_Off.png')
photo_5_On = PhotoImage(file = 'All_Lights Off_On.png')

photo_3 = PhotoImage(file = r"Door_Light_Off.png")
photo_3_On = PhotoImage(file = r"Door_Light_On.png") 

photo_4 = PhotoImage(file = r"Porch_Light_Off.png")
photo_4_On = PhotoImage(file = r"Porch_Light_On.png")

photo_2 = PhotoImage(file = r"Living_Room_Light_Off.png")
photo_2_On = PhotoImage(file = r"Living_Room_Light_On.png")

photo_6 = PhotoImage(file = r"Open_Vents_Off.png")
photo_6_On = PhotoImage(file = r"Close_Vents_On.png")

photo_7 = PhotoImage(file = r"Aqua_Hot_Diesel_Off.png")
photo_7_On = PhotoImage(file = r"Aqua_Hot_Diesel_On.png")

photo_8 = PhotoImage(file = r"Aqua_Hot_Electric_Off.png")
photo_8_On = PhotoImage(file = r"Aqua_Hot_Electric_On.png")

photo_9 = PhotoImage(file = r"Half_Bath_Light_Off.png")
photo_9_On = PhotoImage(file = r"Half_Bath_Light_On.png")

photo_10 = PhotoImage(file = r"Rear_Bath_Light.png")
photo_10_On = PhotoImage(file = r"Rear_Bath_Light_On.png")

photo_11 = PhotoImage(file = r"Road_Light_Off.png")
photo_11_On = PhotoImage(file = r"Road_Light_On.png")

photo_12 = PhotoImage(file = r"Water_Pump_Off.png")
photo_12_On = PhotoImage(file = r"Water_Pump_On.png")

photo_13 = PhotoImage(file = r"DS_Living_Room_Light_Off.png")
photo_13_On = PhotoImage(file = r"DS_Living_Room_Light_On.png")

photo_14 = PhotoImage(file = r"PS_Living_Room_Light_Off.png")
photo_14_On = PhotoImage(file = r"PS_Living_Room_Light_On.png")

output_state = 0


def button1_pressed() :#Bedroom light
    global B_state_1

    if  B_state_1 == 3:
        B_state_1 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x0c, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        
    else:
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x0c, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        B_state_1 = 3

def button2_pressed() :#Living Room Light
    global B_state_2
    
    if  B_state_2 == 3:
        B_state_2 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x01, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

    else:
        B_state_2 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x01, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button3_pressed() :#Door_Light
    global B_state_3
    
    if  B_state_3 == 3:
        B_state_3 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x5f, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)  
    else:
        B_state_3 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x5f, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button4_pressed() :#Porch_Light
    global B_state_4
    
    if  B_state_4 == 3:
        B_state_4 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x16, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_4 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x16, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button5_pressed() :#All_Lights_Off
    global B_state_5
    B_state_5 = 2
    button5['image'] = photo_5_On
    
    #Bedroom off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x0c, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg) 
            
    #Half bath ceiling off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x0f, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg)
            
    #Half bath vanity off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x10, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg)
            
    #Rear bath ceiling off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x0d, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg)
         
    #Rear bath vanity off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x11, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg)
          
    #Main ceiling light off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x01, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg)
            
    #Driver ceiling light off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x04, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg)
            
    #Pass ceiling light off
    msg = can.Message(arbitration_id=0x1fedb99,data=[0x03, 0xff, 0xc8, 0x03, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
    bus.send(msg)


def button6_pressed() :#Close / Open Vents
    global B_state_6
    
    if  B_state_6 == 3:
        B_state_6 = 2
        button6['image'] = photo_6_On

        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1b, 0xff, 0x0, 0x3, 0x0, 0x0, 0xff, 0xff],is_extended_id=True)#Open Galley
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1a, 0xff, 0xc8, 0x1, 0x14, 0x0, 0xff, 0xff],is_extended_id=True)#Open Galley
        bus.send(msg)
        time.sleep(0.5)
        msg = can.Message(arbitration_id=0x1fed996,data=[0x27, 0xff, 0x0, 0xff, 0xff, 0xff, 0x3, 0xff],is_extended_id=True)#Open Galley indicator on
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1f, 0xff, 0x0, 0x3, 0x0, 0x0, 0xff, 0xff],is_extended_id=True)#Open mid vent
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1e, 0xff, 0xc8, 0x1, 0x14, 0x0, 0xff, 0xff],is_extended_id=True)#Open mid vent
        bus.send(msg)
        time.sleep(0.5)
        msg = can.Message(arbitration_id=0x1fed996,data=[0x36, 0xff, 0x0, 0xff, 0xff, 0xff, 0x3, 0xff],is_extended_id=True)#Open Mid vent indicator on
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x22, 0xff, 0x0, 0x3, 0x0, 0x0, 0xff, 0xff],is_extended_id=True)#Open Galley
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x21, 0xff, 0xc8, 0x1, 0x14, 0x0, 0xff, 0xff],is_extended_id=True)#Open Galley
        bus.send(msg)
        time.sleep(0.5)
        msg = can.Message(arbitration_id=0x1fed996,data=[0x72, 0xff, 0x0, 0xff, 0xff, 0xff, 0x3, 0xff],is_extended_id=True)#Rear vent indicator on
        bus.send(msg)
    else:
        B_state_6 = 3
        button6['image'] = photo_6
        
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1a, 0xff, 0x0, 0x3, 0x0, 0x0, 0xff, 0xff],is_extended_id=True)#Close Galley
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1b, 0xff, 0xc8, 0x1, 0x14, 0x0, 0xff, 0xff],is_extended_id=True)#Close Galley
        bus.send(msg)
        time.sleep(0.5)
        msg = can.Message(arbitration_id=0x1fed996,data=[0x27, 0xff, 0x0, 0xff, 0xff, 0xff, 0x2, 0xff],is_extended_id=True)#Galley indicator off
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1e, 0xff, 0x0, 0x3, 0x0, 0x0, 0xff, 0xff],is_extended_id=True)#Close mid vent
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x1f, 0xff, 0xc8, 0x1, 0x14, 0x0, 0xff, 0xff],is_extended_id=True)#Close mid vent
        bus.send(msg)
        time.sleep(0.5)
        msg = can.Message(arbitration_id=0x1fed996,data=[0x36, 0xff, 0x0, 0xff, 0xff, 0xff, 0x2, 0xff],is_extended_id=True)#Mid vent indicator off
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x21, 0xff, 0x0, 0x3, 0x0, 0x0, 0xff, 0xff],is_extended_id=True)#Close Rear vent
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb9d,data=[0x22, 0xff, 0xc8, 0x1, 0x14, 0x0, 0xff, 0xff],is_extended_id=True)#Close Rear vent
        bus.send(msg)
        time.sleep(0.5)
        msg = can.Message(arbitration_id=0x1fed996,data=[0x72, 0xff, 0x0, 0xff, 0xff, 0xff, 0x2, 0xff],is_extended_id=True)# Rear vent indicator off
        bus.send(msg)

def button7_pressed() :#Aqua_Hot_Diesel
    global B_state_7

    if  B_state_7 == 3:
        B_state_7 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x18, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_7 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x18, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button8_pressed() :#Aqua_Hot_Electric
    global B_state_8
    
    if  B_state_8 == 3:
        B_state_8 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x17, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_8 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x17, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button9_pressed() :#Half_Bath_Light
    global B_state_9
    
    if  B_state_9 == 3:
        B_state_9 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x0f, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x10, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        
    else:
        B_state_9 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x0f, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x10, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button10_pressed() :#Rear_bath_light
    global B_state_10
    
    if  B_state_10 == 3:
        B_state_10 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0xd, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x11, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_10 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0xd, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x11, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        

def button11_pressed() :#Road_light
    global B_state_11
    
    if  B_state_11 == 3:
        B_state_11 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x15, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_11 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x15, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button12_pressed() :#Water_pump
    global B_state_12
    
    if  B_state_12 == 3:
        B_state_12 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x5d, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_12 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x5d, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

def button13_pressed() :#Driver ceiling light off
    global B_state_13
    
    if  B_state_13 == 3:
        B_state_13 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x4, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_13 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x4, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
        

def button14_pressed() :#Pass ceiling light off
    global B_state_14
    
    if  B_state_14 == 3:
        B_state_14 = 2
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x3, 0xff, 0xc8, 0x2, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)
    else:
        B_state_14 = 3
        msg = can.Message(arbitration_id=0x1fedb99,data=[0x3, 0xff, 0xc8, 0x3, 0xff, 0x00, 0xff, 0xff],is_extended_id=True)
        bus.send(msg)

        
        
def can_rx_task():
    while True:
        message = bus.recv()
        q.put(message)

button1 = tkinter.Button(master,image = photo_1, command = button1_pressed )
button1.grid(row=1,column=0)

button2=tkinter.Button(master,image = photo_2 ,command = button2_pressed)
button2.grid(row=1,column=1)

button3=tkinter.Button(master ,image = photo_3 ,command = button3_pressed )
button3.grid(row=3,column=0)

button4=tkinter.Button(master,image = photo_4 , command = button4_pressed)
button4.grid(row=3,column=1)

button5=tkinter.Button(master ,image = photo_5 , command = button5_pressed)
button5.grid(row=4,column=0)

button6=tkinter.Button(master ,image = photo_6 , command = button6_pressed)
button6.grid(row=4,column=1)

button7=tkinter.Button(master ,image = photo_7, command = button7_pressed )
button7.grid(row=5,column=0)

button8=tkinter.Button(master ,image = photo_8 , command = button8_pressed)
button8.grid(row=5,column=1)

button9=tkinter.Button(master ,image = photo_9 , command = button9_pressed)
button9.grid(row=6,column=0)

button10=tkinter.Button(master,image = photo_10 , command = button10_pressed)
button10.grid(row=6,column=1)

button11=tkinter.Button(master ,image = photo_11 , command = button11_pressed)
button11.grid(row=7,column=0)

button12=tkinter.Button(master ,image = photo_12 , command = button12_pressed)
button12.grid(row=7,column=1)

button13=tkinter.Button(master ,image = photo_13 , command = button13_pressed)
button13.grid(row=2,column=0)

button14=tkinter.Button(master ,image = photo_14 , command = button14_pressed)
button14.grid(row=2,column=1)



def can_decode_task():
    global B_state_1
    global B_state_2
    global B_state_3
    global B_state_4
    global B_state_5
    global B_state_6
    global B_state_7
    global B_state_8
    global B_state_9
    global B_state_10
    global B_state_11
    global B_state_12
    global B_state_13
    global B_state_14
    
    global output_state
    global output_value
    global Bedroom_icon_time_On
    global Door_icon_time_On
    global Porch_icon_time_On
    global Road_icon_time_On
    global Diesel_icon_time_On
    global Electric_icon_time_On
    global Water_pump_icon_time_On
    global Living_Room_icon_time_On
    global Rear_Bath_icon_time_On
    global Half_Bath_icon_time_On
    global DS_Living_Room_icon_time_On
    global PS_Living_Room_icon_time_On
    Present_time = 0.0
    output_value = 0
    output_state = 0
    Bedroom_icon_time_On = 0.0
    Porch_icon_time_On = 0.0
    Road_icon_time_On = 0.0
    Door_icon_time_On = 0.0
    Diesel_icon_time_On = 0.0
    Electric_icon_time_On = 0.0
    Water_pump_icon_time_On = 0.0
    Living_Room_icon_time_On = 0.0
    Rear_Bath_icon_time_On = 0.0
    Half_Bath_icon_time_On = 0.0
    DS_Living_Room_icon_time_On = 0.0
    PS_Living_Room_icon_time_On = 0.0


#Spyder system transmits ~ 2 seconds the state of an output when On, there is no transmission if output is Off.

    while True:
        
        
            if q.empty() != True:# Check if there is a message in queue
                message = q.get()
                Present_time = time.time()
            
                for i in range(message.dlc ):
                    if i == 0:
                        output_state =(message.data[i])
                    if i == 5:
                        output_value ='{0:x} '.format(message.data[i])

                        
            if (output_state == 0xc):#Bedroom light
            
                B_state_1 = (output_value) #present state of output
            
                if B_state_1 == 3:
                    button1['image'] = photo_1
                
                else:
                    button1['image'] = photo_1_On
                    B_state_1 = 2
                    Bedroom_icon_time_On = time.time() + 3.0
 
            if (output_state == 0x16):#Porch light
            
                B_state_4 = (output_value) #present state of output

                if B_state_4 == 3:#Porch_Light
                    button4['image'] = photo_4

                else:
                    button4['image'] = photo_4_On
                    B_state_4 = 2
                    Porch_icon_time_On = time.time() + 3.0

            if (output_state == 0x5f):#Door light
            
                B_state_3 = (output_value) #present state of output
            
                if B_state_3 == 3:
                    button3['image'] = photo_3                
                else:
                    button3['image'] = photo_3_On
                    Door_icon_time_On = time.time() + 3.0

            if (output_state == 0x18):#Aqua hot Diesel
            
                B_state_7 = (output_value) #present state of output
            
                if B_state_7 == 3:
                    button7['image'] = photo_7
                
                else:
                    button7['image'] = photo_7_On
                Diesel_icon_time_On = time.time() + 3.0

            if (output_state == 0x17):#Aqua hot Electric
            
                B_state_8 = (output_value) #present state of output
            
                if B_state_8 == 3:
                    button8['image'] = photo_8
                
                else:
                    button8['image'] = photo_8_On
                    Electric_icon_time_On = time.time() + 3.0

            if (output_state == 0x5d):#Water pump
            
                B_state_12 = (output_value) #present state of output
            
                if B_state_12 == 3:
                    button12['image'] = photo_12
                
                else:
                    button12['image'] = photo_12_On
                    Water_pump_icon_time_On = time.time() + 3.0


            if (output_state == 0x1):#Living Room light
            
                B_state_2 = (output_value) #present state of output
            
                if B_state_2 == 3:
                    button2['image'] = photo_2
                
                else:
                    button2['image'] = photo_2_On
                    Living_Room_icon_time_On = time.time() + 3.0
                    
            if (output_state == 0x15):#Road light
            
                B_state_11 = (output_value) #present state of output

                if B_state_11 == 3:#Road_Light
                    button11['image'] = photo_11

                else:
                    button11['image'] = photo_11_On
                    B_state_11 = 2
                    Road_icon_time_On = time.time() + 3.0

                   
            if (output_state == 0x4):#DS living room light light
            
                B_state_13 = (output_value) #present state of output

                if B_state_13 == 3:#Road_Light
                    button13['image'] = photo_13

                else:
                    button13['image'] = photo_13_On
                    B_state_13 = 2
                    DS_Living_Room_icon_time_On = time.time() + 3.0

                          
            if (output_state == 0x3):#PS living room light light
            
                B_state_14 = (output_value) #present state of output

                if B_state_14 == 3:#
                    button14['image'] = photo_14

                else:
                    button14['image'] = photo_14_On
                    B_state_14 = 2
                    PS_Living_Room_icon_time_On = time.time() + 3.0

                  
                    
            if (output_state == 0x11):#Rear bath light use only one output or it takes 2 clicks to turn off icon
                
                B_state_10 =2
                button10['image'] = photo_10_On
                Rear_Bath_icon_time_On = time.time() + 3.0

            if (output_state == 0x10):#Half bath light use only one output or it takes 2 clicks to turn off icon
                
                B_state_9 = 2
                button9['image'] = photo_9_On
                Half_Bath_icon_time_On = time.time() + 3.0


            if B_state_5 == 2:# All lights off icon
                time.sleep(1.0)# need to have all lights on icon on for 1 second
                print ('turn off all')
                button5['image'] = photo_5
                B_state_5 = 3



            if  Present_time > Bedroom_icon_time_On:# Bedroom light icon off
                button1['image'] = photo_1
                B_state_1 = 3

            if  Present_time > Living_Room_icon_time_On:# Living Room light icon off
                button2['image'] = photo_2
                B_state_2 = 3

            if  Present_time > Door_icon_time_On:# Door light icon off
                button3['image'] = photo_3
                B_state_3 = 3

            if  Present_time > Porch_icon_time_On:# Porch light icon off
                button4['image'] = photo_4
                B_state_4 = 3

            if  Present_time > Diesel_icon_time_On:# Diesel light icon off
                button7['image'] = photo_7
                B_state_7 = 3

            if  Present_time > Electric_icon_time_On:# Electric light icon off
                button8['image'] = photo_8
                B_state_8 = 3

            if  Present_time > Water_pump_icon_time_On:# Water pump icon off
                button12['image'] = photo_12
                B_state_12 = 3
                
            if Present_time > Rear_Bath_icon_time_On:#Rear bath light
                button10['image'] = photo_10
                B_state_10 = 3
                
            if Present_time > Half_Bath_icon_time_On:#Half bath light
                button9['image'] = photo_9
                B_state_9 = 3
                
            if Present_time > Road_icon_time_On:#Road light
                button11['image'] = photo_11
                B_state_11 = 3
                
                
            if  Present_time > DS_Living_Room_icon_time_On:# Living Room light icon off
                button13['image'] = photo_13
                B_state_13 = 3


            if  Present_time > PS_Living_Room_icon_time_On:# Living Room light icon off
                button14['image'] = photo_14
                B_state_14 = 3



q = queue.Queue()
t = Thread(target = can_rx_task)# Start receive thread
d = Thread(target = can_decode_task)# Start decode thread
t.start()
d.start()

master.mainloop()






