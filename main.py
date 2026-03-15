import os
from engine.features import *
from engine.command import *
import eel  # eel is use to connect html,css,js with python

eel.init("www") # this is use to show the directory 

playAssistantSound()

os.system('start "" msedge.exe --app="http://localhost:8000/index.html"') #edge is took because it is bydefault in every system

eel.start("index.html", mode='none' , host="localhost",block=True)