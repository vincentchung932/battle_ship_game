import time
def verify_coor(index):
    while 1:
        if index > 4 or index <0:
            print("It should be < 4 and >0")
            index = int(input("Enter x coordinate: "))
        else:
            return index
        
        
def place_ship(x,y,dir):
    ship_coordinate = [[y,x]]
    if dir == "V":
        if y - 1 < 0:
            ship_coordinate.append([y+1,x])
            ship_coordinate.append([y+2,x])
        elif y + 1 > 4:
            ship_coordinate.append([y-1,x])
            ship_coordinate.append([y-2,x])
        else:
            ship_coordinate.append([y+1,x])
            ship_coordinate.append([y-1,x])
    elif dir =="H":
        if x - 1 < 0:
            ship_coordinate.append([y,x+1])
            ship_coordinate.append([y,x+2])
        elif x + 1 > 4:
            ship_coordinate.append([y,x-1])
            ship_coordinate.append([y,x-2])
        else:
            ship_coordinate.append([y,x+1])
            ship_coordinate.append([y,x-1])
    return ship_coordinate

def count_down(sec):
    for i in range(sec,0,-1):
        print(f"{i}")
        time.sleep(1)


def print_win():
    print("_____.___.               __      __.__         ._._._.")
    print("\__  |   | ____  __ __  /  \    /  \__| ____   | | | |")
    print(" /   |   |/  _ \|  |  \ \   \/\/   /  |/    \  | | | |")
    print(" \____   (  <_> )  |  /  \        /|  |   |  \  \|\|\|")
    print(" / ______|\____/|____/    \__/\  / |__|___|  /  ______")
    print(" \/                            \/          \/   \/\/\/")

def print_loss():
    print("_____.___.              .____    ________    _________ _________ ._._._.")
    print("\__  |   | ____  __ __  |    |   \_____  \  /   _____//   _____/ | | | |")
    print(" /   |   |/  _ \|  |  \ |    |    /   |   \ \_____  \ \_____  \  | | | |")
    print(" \____   (  <_> )  |  / |    |___/    |    \/        \/        \  \|\|\|")
    print(" / ______|\____/|____/  |_______ \_______  /_______  /_______  /  ______")
    print(" \/                             \/       \/        \/        \/   \/\/\/")