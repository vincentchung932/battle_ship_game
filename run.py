from lib.ship import *
from lib.func import *
import time
import os
import random

print("    __ __ __ ____   ___ ____  __  _____     ____   ____ ______ ______ _       ___       _______ __ ____ ____  ")
print("   /  ]  |  |    | /  _]    \|  |/ ___/    |    \ /    |      |      | |     /  _]     / ___/  |  |    |    \ ")
print("  /  /|  |  ||  | /  [_|  _  |_ (   \_     |  o  )  o  |      |      | |    /  [_     (   \_|  |  ||  ||  o  )")
print(" /  / |  _  ||  ||    _]  |  | \|\__  |    |     |     |_|  |_|_|  |_| |___|    _]     \__  |  _  ||  ||   _/ ")
print("/   \_|  |  ||  ||   [_|  |  |   /  \ |    |  O  |  _  | |  |   |  | |     |   [_      /  \ |  |  ||  ||  |   ")
print("\     |  |  ||  ||     |  |  |   \    |    |     |  |  | |  |   |  | |     |     |     \    |  |  ||  ||  |   ")
print(" \____|__|__|____|_____|__|__|    \___|    |_____|__|__| |__|   |__| |_____|_____|      \___|__|__|____|__|   ")
print("")

print("Your ship and  pirate's ship are placed in a 5x5 map.")
print("The size of ship should be 1x3. It can be placed horizontally or vertically.")
print("Try to guess the coordinate of the pirate's ship and sink it!")
print("")
print("Enter a coordinate to place your ship. (x,y), where (x =0~4, y=0~4) ")
coordinate_x = int(input("Enter x coordinate: "))
coordinate_x = verify_coor(coordinate_x)
coordinate_y = int(input("Enter y coordinate: "))
coordinate_y = verify_coor(coordinate_y)
direction = input("Choose your direction(H for horizontally and V for vertically: ")
ship_coordinate = place_ship(coordinate_x,coordinate_y,direction)
print("OK, the battle field has been set. Let's go battle!")
count_down(3)
os.system("cls")
#####################################################################################
#####################################################################################
pirate_coordinate = place_ship(random.randint(0, 4),random.randint(0, 4),random.choice(["V","H"]))

user_ship = Ship(ship_coordinate)
pirate_ship = Ship2(pirate_coordinate)

while 1:
    if user_ship.check_if_sink():
        print_loss()
        break
    if pirate_ship.check_if_sink():
        print_win()
        break
    
    user_ship.print_situation()
    pirate_ship.print_situation()

    user_ship.hit_enemy(pirate_ship)
    pirate_ship.hit_enemy(user_ship)
    
    print("Cannonball is flying................")
    time.sleep(1)
    print("Printing current battle situation.................")
    time.sleep(1)
    
    


