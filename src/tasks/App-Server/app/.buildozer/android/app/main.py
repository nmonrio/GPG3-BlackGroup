#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:55:16 2021

@author: bernat
"""

import socket

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label

class MyGrid(GridLayout):

    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=3
        
        self.ip = TextInput(multiline=False,text="127.0.0.1")
        self.add_widget(self.ip)
        
        self.port = TextInput(multiline=False,text="65433")
        self.add_widget(self.port)
        
        self.connect = Button(text="Connect",font_size=40)
        self.connect.bind(on_press=self.startClient)
        self.add_widget(self.connect) 
                
        self.forLeft = Button(text="Left Forward",font_size=40)
        self.forLeft.bind(on_press=self.forwardLeft)
        self.add_widget(self.forLeft)   

        self.forward = Button(text="Forward",font_size=40)
        self.forward.bind(on_press=self.goForward)
        self.add_widget(self.forward)   

        self.forRight = Button(text="Right Forward",font_size=40)
        self.forRight.bind(on_press=self.forwardRight)
        self.add_widget(self.forRight) 
        
        self.turnLeft = Button(text="Left",font_size=40)
        self.turnLeft.bind(on_press=self.left)
        self.add_widget(self.turnLeft) 
     
        self.stop = Button(text="Stop",font_size=40)
        self.stop.bind(on_press=self.stopHere)
        self.add_widget(self.stop)
        
        self.turnRight = Button(text="Right",font_size=40)
        self.turnRight.bind(on_press=self.right)
        self.add_widget(self.turnRight) 
 
        self.backLeft = Button(text="Left Back",font_size=40)
        self.backLeft.bind(on_press=self.backwardLeft)
        self.add_widget(self.backLeft) 
        
        self.backward = Button(text="Backward",font_size=40)
        self.backward.bind(on_press=self.goBackward)
        self.add_widget(self.backward) 
        
        self.backRight = Button(text="Right Back",font_size=40)
        self.backRight.bind(on_press=self.backwardRight)
        self.add_widget(self.backRight) 
        
        self.program1 = Button(text="Program 1",font_size=40)
        self.program1.bind(on_press=self.program_1)
        self.add_widget(self.program1)
        
        self.program2 = Button(text="Program 2",font_size=40)
        self.program2.bind(on_press=self.program_2)
        self.add_widget(self.program2)
        
        self.program3 = Button(text="Program 3",font_size=40)
        self.program3.bind(on_press=self.program_3)
        self.add_widget(self.program3)
        
    def startClient(self, *args):
        try:
            HOST = '127.0.0.1'  # The server's hostname or IP address
            HOST = self.ip.text
            PORT = 65433  # The port used by the server
            PORT = int(self.port.text)
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
            print("Connected")
        except:
            print("Could not connect")
        
    def forwardLeft(self,instance):
        try:
            print("Sent: Forward Left")
            self.s.sendall(bytes("q", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def goForward(self,instance):
        try: 
            print("Sent: Forward")
            self.s.sendall(bytes("w", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")
        
    def forwardRight(self,instance):
        try:
            print("Sent: Forward Right")
            self.s.sendall(bytes("e", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def left(self,instance):
        try:
            print("Sent: Left")
            self.s.sendall(bytes("a", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def stopHere(self,instance):
        try:
            print("Sent: Stop")
            self.s.sendall(bytes(" ", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def right(self,instance):
        try:
            print("Sent: Right")
            self.s.sendall(bytes("d", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def backwardLeft(self,instance):
        try:
            print("Sent: Backward Left")
            self.s.sendall(bytes("z", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def goBackward(self,instance):
        try:
            print("Sent: Backward")
            self.s.sendall(bytes("s", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")
        
    def backwardRight(self,instance):
        try:
            print("Sent: Backward Right")
            self.s.sendall(bytes("x", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")
    
    def program_1(self,instance):
        try:
            print("Sent: Program 1")
            self.s.sendall(bytes("1", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def program_2(self,instance):
        try:
            print("Sent: Program 2")
            self.s.sendall(bytes("2", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

    def program_3(self,instance):
        try:
            print("Sent: Program 3")
            self.s.sendall(bytes("3", 'utf-8'))
            data = repr(self.s.recv(1024))
            datarefined = data[2:len(data)-1:]
            print('Received: Executing', datarefined)
        except:
            print("Not Connected")

class RaspberryApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    RaspberryApp().run()