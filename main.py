#practica de Kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider

class DividedWindowApp(App):
    def build(self):
        # Crear un GridLayout para dividir la ventana en 4 partes
        layout = GridLayout(cols=2, rows=2, padding=10, spacing=10)



if __name__ == "__main__":
     DividedWindowApp().run()