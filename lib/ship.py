from lib.func import verify_coor
import random
import time

class Ship():
    def __init__(self, ship_coordinate,hit_coordinate=[]):
        self.ship_coordinate = ship_coordinate
        self.hit_coordinate = hit_coordinate
    
    def print_situation(self):
        print("Your Ship:")
        for i in range(5):
            for j in range(5):
                if [i,j] in self.hit_coordinate and [i,j] in self.ship_coordinate:
                    print("✓",end=" ")
                elif [i,j] in self.hit_coordinate:
                    print("X",end=" ")
                elif [i,j] in self.ship_coordinate:
                    print("0",end=" ")
                else:
                    print("'",end=" ")
            print("")
    
    def check_if_sink(self):
        if(all(coor in self.hit_coordinate for coor in self.ship_coordinate)):
            return True
    
    def hit_enemy(self,other):
        print("Let's hit the pirate")
        x = int(input("Enter x coordinate you want to hit: "))
        x = verify_coor(x)
        y = int(input("Enter y coordinate you want to hit: "))
        y = verify_coor(y)
        other.hit_coordinate.append([y,x])
        print(f"You hit [{x},{y}]")



class Ship2(Ship):
    def __init__(self, ship_coordinate, hit_coordinate=[]):
        super().__init__(ship_coordinate, hit_coordinate =[])
    
    def print_situation(self):
        print("Pirate Ship:")
        for i in range(5):
            for j in range(5):
                if [i,j] in self.hit_coordinate and [i,j] in self.ship_coordinate:
                    print("✓",end=" ")
                elif [i,j] in self.hit_coordinate:
                    print("X",end=" ")
                # elif [i,j] in self.ship_coordinate:
                #     print("0",end=" ")
                else:
                    print("'",end=" ")
            print("")
    
    def hit_enemy(self,other):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        other.hit_coordinate.append([y,x])
        print(f"Pirate hit [{x},{y}]")
    
    def show_result(self):
        print("The Pirate got away!!")
        for i in range(5):
            for j in range(5):
                if [i,j] in self.hit_coordinate and [i,j] in self.ship_coordinate:
                    print("✓",end=" ")
                elif [i,j] in self.hit_coordinate:
                    print("X",end=" ")
                elif [i,j] in self.ship_coordinate:
                    print("0",end=" ")
                else:
                    print("'",end=" ")
            print("")