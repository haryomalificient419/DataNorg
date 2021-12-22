from view import *
from datawriter import Csv

from dataclasses import dataclass



class DataNorg(App):
    def build(self) -> object:
        self.icon = 'datanorg.png'
        screen_manager = ScreenManager(transition = FadeTransition ())
        start_screen = Start(name="start")
        data_entry_screen = DataEntry(name="dataentry")
        screen_manager.add_widget(start_screen)
        screen_manager.add_widget(data_entry_screen)
        return screen_manager


if __name__ == "__main__":
    app = DataNorg()
    app.run()




