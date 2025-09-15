from django.shortcuts import render
from dice_roller import *
# Create your views here.


def dcc_stats(roll_type):
    character_stats = {}
    stats = ["str", "dex", "con", "int", "per", "luck"]
    if roll_type == "D": # Default
        for key in stats:
            character_stats[key] = sum(roll_XdY(3, 6))
    elif roll_type == "H": # Heroic
        for key in stats:
            character_stats[key] = sum(roll_XdYdl_Z(4, 6, 1))
    return character_stats

print(dcc_stats("H"))