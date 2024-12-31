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
        # Sección 1: Botón
        button = Button(text="Soy un Botón", size_hint=(0.5, 0.5))
        layout.add_widget(button)
        # Sección 2: Etiqueta
        label = Label(text="Soy una Etiqueta", size_hint=(0.5, 0.5))
        layout.add_widget(label)
        # Sección 3: Campo de texto
        text_input = TextInput(hint_text="Escribe algo aquí", size_hint=(0.5, 0.5))
        layout.add_widget(text_input)
        # Sección 4: Slider
        slider = Slider(min=0, max=100, value=50, size_hint=(0.5, 0.5))
        layout.add_widget(slider)
        return layout



if __name__ == "__main__":
     DividedWindowApp().run()