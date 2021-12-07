from dataclasses import dataclass
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Start(Screen):
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)

class DataEntry(Screen):
    def __init__(self, **kwargs):
        super(DataEntry, self).__init__(**kwargs)

class DataNorg(App):
    def build(self):
        self.icon = 'datanorg.png'
        screen_manager = ScreenManager()
        start_screen = Start(name="start")
        data_entry_screen = DataEntry(name="dataentry")
        screen_manager.add_widget(start_screen)
        screen_manager.add_widget(data_entry_screen)
        
        return screen_manager


