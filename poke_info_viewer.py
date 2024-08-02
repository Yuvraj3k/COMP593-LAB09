""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""

from tkinter import Tk, ttk, messagebox
from poke_api import get_pokemon_info


# Create the main window
root = Tk()
root.title("Pokemon Information")
root.resizable(False,False)
# Create the frames
input = ttk.Frame(root)
input.grid(row=0, column=0, columnspan=2, pady=(20,10))
#frame for info
info=ttk.LabelFrame(root, text='info')
info.grid(row=1,column=0,padx=(20,10),pady=(10,20), sticky='N' )

#frame for stats 
stats=ttk.LabelFrame(root, text='stats')
stats.grid(row=1,column=1,padx=(10,20),pady=(10,20), sticky='N') 
# Populate the user input frame with widgets


# TODO: Define button click event handler function

root.mainloop()