import os
import renamer_ui
import home_ui
import fuser_ui

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
GLOBAL_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = {
    "renamer" : os.path.join(GLOBAL_DIR, "renamer.ui"),
    "home" : os.path.join(GLOBAL_DIR, "home.ui"),
}

PAGES_UI = {
    "renamer" : renamer_ui.Ui_home(),
    "home" : home_ui.Ui_Autorenamer(),
    "fuser" : fuser_ui.Ui_fuser()
}

PAGES_INDEX = {
    "home" : 0,
    "renamer" : 1
}

PAGES_TITLES = {
    "home" : 'Autorenamer',
}

FILE_DIALOG_CAPTION = "Choisissez le dossier à organiser - Autorenamer"

TYPE_VIDEOS = ['vf', 'vostfr']
BAD_NAME_WORDS = TYPE_VIDEOS.copy()
BAD_NAME_WORDS.extend(['ep','episode','s','saison','season','#new','voiranime','fin','hd','mp'])