import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)

		self.inside = GridLayout()
		self.inside.cols = 2
		self.inside.rows = 2
		self.inside.add_widget(Label(text=""))
		self.inside.add_widget(Label(text=""))


		self.cols = 2
		self.add_widget(self.inside)
		self.add_widget (Button(text="Submit"))

class PaintWindow(Widget):
	pass

class PaintApp(App):
	def build(self):
		return MyGrid()



if __name__=="__main__":
	#n = int(input("Tell me precission: \n"))
	PaintApp().run()