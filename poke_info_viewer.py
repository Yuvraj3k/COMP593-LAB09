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

# Create the frames
input = ttk.Frame(root)
input.grid(row=0, column=0, columnspan=2)

info = ttk.LabelFrame(root, text="Info")
info.grid(row=1, column=0, sticky="N", padx=(5, 10), pady=(5, 10))

stats = ttk.LabelFrame(root, text="Stats")
stats.grid(row=1, column=1, sticky="N", padx=(5, 10), pady=(5, 10))


# Populate the user input frame with widgets
input_lbl = ttk.Label(input, text="Pokemon Name:")
input_lbl.grid(row=0, column=0, padx=(10,5), pady=10)

input_ent = ttk.Entry(input)
input_ent.grid(row=0 ,column=1, padx=5, pady=10)

# TODO: Define button click event handler function

root.mainloop()