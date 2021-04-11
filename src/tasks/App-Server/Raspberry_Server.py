#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:08:28 2021

@author: bernat
"""

#!/usr/bin/env python3

import socket
#import time    # import the time library for the sleep function
#import gopigo3 # import the GoPiGo3 drivers
HOST = '127.0.0.1'
#HOST = '10.10.10.10'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)
#GPG = gopigo3.GoPiGo3() 

def forward():
    pass

def backward():
    pass

def left():
    pass

def right():
    pass

def forwardRight():
    pass

def forwardLeft():
    pass

def backwardRight():
    pass

def backwardLeft():
    pass

def stop():
    pass

def program1():
    pass

def program2():
    pass

def program3():
    pass

if __name__=="__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True: #Add timeout to this infinite loop
            conn, addr = s.accept() 
            with conn:
                print('Connected by', addr)
                while True:
                    rawdata = conn.recv(1024)
                    data = repr(rawdata)
                    datarefined = data[2:len(data)-1:]
                    print("Received",datarefined)
                    if not rawdata: #fix this so it isn't so brute force
                        break
                    if datarefined == "w":
                        conn.sendall(bytes("Forward", 'utf-8'))
                        forward()
                    elif datarefined == "s":
                        conn.sendall(bytes("Backward", 'utf-8'))
                        backward()
                    elif datarefined == "a":
                        conn.sendall(bytes("Left", 'utf-8'))
                        left()
                    elif datarefined == "d":
                        conn.sendall(bytes("Right", 'utf-8'))
                        right()
                    elif datarefined == "q":
                        conn.sendall(bytes("Forward Left", 'utf-8'))
                        forwardLeft()
                    elif datarefined == "e":
                        conn.sendall(bytes("Forward Right", 'utf-8'))
                        forwardRight()
                    elif datarefined == "z":
                        conn.sendall(bytes("Backward Left", 'utf-8'))
                        backwardLeft()
                    elif datarefined == "x":
                        conn.sendall(bytes("Backward Right", 'utf-8'))
                        backwardRight()
                    elif datarefined == " ":
                        conn.sendall(bytes("Stop", 'utf-8'))
                        stop()                    
                    elif datarefined == "1":
                        conn.sendall(bytes("Program 1", 'utf-8'))
                        program1()
                    elif datarefined == "2":
                        conn.sendall(bytes("Program 2", 'utf-8'))
                        program2()
                    elif datarefined == "3":
                        conn.sendall(bytes("Program 3", 'utf-8'))
                        program3()
                    else:
                        conn.sendall(bytes("Unknown", 'utf-8'))
