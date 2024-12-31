from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class DividedWindowApp(App):
    def build(self):
        # Definir la raíz desde el archivo .kv
        return DividedWindow()

class DividedWindow(GridLayout):
    button = ObjectProperty(None)
    label = ObjectProperty(None)
    text_input = ObjectProperty(None)
    slider = ObjectProperty(None)

if __name__ == "__main__":
    DividedWindowApp().run()
