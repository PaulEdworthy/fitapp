from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp


colors = {
    'Red': {
        '200': 'EC1A1A',
        '500': 'EC1A1A',
        '700': 'EC1A1A'
    }
}

class MainApp(MDApp):
    #Window.clearcolor = (51 / 255, 51 / 255, 51 / 255, 1)
    Window.size = [385, 800]
    Window.top = 200
    Window.left = 100

    data = {
        'New workout': 'new-box',
        'Add manual': 'pencil',
        'Repeat': 'repeat'
    }


    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'

        return Builder.load_file('main.kv')


if __name__ == "__main__":
    MainApp().run()
