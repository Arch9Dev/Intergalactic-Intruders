from settings import show_settings
from play import show_play
from main import main_menu
from intro  import show_intro
from levels import show_levels


class pagelist():
    def __init__(self,PageName) -> None:
        self.PageName =  PageName.upper()
    def switching(self):
    
        if self.PageName ==  "MAIN":
             main_menu()
        elif self.PageName == "PLAY":
            show_play()
        elif self.PageName == "SETTINGS":
            show_settings()
        elif self.PageName == "TUTORIAL":
            show_intro()
        elif self.PageName == "LEVELS":
            show_levels()
      

  



