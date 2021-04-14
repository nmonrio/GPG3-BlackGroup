 
import socket

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.clock import Clock

from functools import partial

class MainWindow(Screen):
	pass

class ButtonWindow(Screen):
	pass

class SendCommands():
	def startClient(self, host_name, port_name):
		try:
			HOST = '127.0.0.1'  # The server's hostname or IP address (this is the default)
			HOST = host_name
			PORT = 65433  # The port used by the server (this is the default)
			PORT = int(port_name)
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.connect((HOST, PORT))
			print("Connected")
			successPopup()
		except:
			print("Could not connect")
			errorPopup()

	def sendMessage(self,command):
		try:
			print("Sent:",command)
			self.s.sendall(bytes(str(command), 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

'''
class SendCommand():
	def startClient(self, *args):
		#try:
		HOST = '127.0.0.1'  # The server's hostname or IP address
		PORT = 65433  # The port used by the server
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((HOST, PORT))
		print("Connected")
		successPopup()
		#except:
		#	print("Could not connect")
		#	errorPopup()
	#Buttons:
	def forwardLeft(self):
		try:
			print("Sent: Forward Left")
			self.s.sendall(bytes("q", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def goForward(self):
		try: 
			print("Sent: Forward")
			self.s.sendall(bytes("w", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def forwardRight(self):
		try:
			print("Sent: Forward Right")
			self.s.sendall(bytes("e", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def left(self):
		try:
			print("Sent: Left")
			self.s.sendall(bytes("a", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def stopHere(self):
		try:
			print("Sent: Stop")
			self.s.sendall(bytes(" ", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def right(self):
		try:
			print("Sent: Right")
			self.s.sendall(bytes("d", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def backwardLeft(self):
		try:
			print("Sent: Backward Left")
			self.s.sendall(bytes("z", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def goBackward(self):
		try:
			print("Sent: Backward")
			self.s.sendall(bytes("s", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def backwardRight(self):
		try:
			print("Sent: Backward Right")
			self.s.sendall(bytes("x", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def program_1(self):
		try:
			print("Sent: Program 1")
			self.s.sendall(bytes("1", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def program_2(self):
		try:
			print("Sent: Program 2")
			self.s.sendall(bytes("2", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	def program_3(self):
		try:
			print("Sent: Program 3")
			self.s.sendall(bytes("3", 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Received: Executing', datarefined)
		except:
			print("Not Connected")

	#Sliders:
	def leftSlider(self,value):
		try:
			print("Sent: Left Slider",value)
			self.s.sendall(bytes("l"+str(value), 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Left Motor Set to:', datarefined)
		except:
			print("Not Connected")
	
	def rightSlider(self,value):
		try:
			print("Sent: Right Slider",value)
			self.s.sendall(bytes("l"+str(value), 'utf-8'))
			data = repr(self.s.recv(1024))
			datarefined = data[2:len(data)-1:]
			print('Right Motor Set to:', datarefined)
		except:
			print("Not Connected")
	pass
'''

class SliderWindow(Screen):
	
	active = False
	prev_left = "#"
	prev_right = "#"

	def send_values(self,left,right):
		print("l",int(self.left_slider.value),"r",int(self.right_slider.value))
		MyRaspberryApp.send_commands.sendMessage("l"+str(int(self.left_slider.value))+"r"+str(int(self.right_slider.value)))

	pass

class WindowManager(ScreenManager):
	pass

class popupConnectionError(FloatLayout):
	pass
class popupConnectionSuccess(FloatLayout):
	pass

class errorPopup(Popup):
    def __init__(self, **kwargs):
        self.popup = Popup(title = "Error", content = popupConnectionError(), size_hint = (None, None), size = (400,150))
        self.popup.open()
        Clock.schedule_once(self.dismiss_popup, 4)

    def dismiss_popup(self, dt):
        self.popup.dismiss()

class successPopup(Popup):
    def __init__(self, **kwargs):
        self.popup = Popup(title = "Success", content = popupConnectionSuccess(), size_hint = (None, None), size = (400,150))
        self.popup.open()
        Clock.schedule_once(self.dismiss_popup, 2)

    def dismiss_popup(self, dt):
        self.popup.dismiss()



kv = Builder.load_file("main.kv")

class MyRaspberryApp(App):
	send_commands = SendCommands()
	slider_window = SliderWindow()
	main_window = MainWindow()

	def build(self):
		return kv

if __name__=="__main__":
	MyRaspberryApp().run()