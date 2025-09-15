from views import *

def run_dcc_stats():
    print("*"*20,"Choose your poison! Rolling for Stats", 20*"*")
    print("1-Default: 3d6\n2-Heroic: 4d6 drop the lowest\n")
    roll_type = int(input("Type D for Default stat roll or H for Heroic: "))

    return dcc_stats(roll_type)
