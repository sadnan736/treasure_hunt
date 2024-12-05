import random


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Remember, this game is randomized every time. So no cheating.")

#paths
path1 = ['left', 'right']
path2 = ['swim', 'build']
path3 = ['blue', 'yellow', 'red']

# correct paths
path1_ans = random.choice(path1)
path2_ans = random.choice(path2)
path3_ans = random.choice(path3)

class Path:
    def __init__(self) -> None:
        self.choice1 = None
        self.choice2 = None
        self.choice3 = None
        self.win = False
    
    
    def path1_journey(self, path1, path1_ans, path2, path2_ans, path3, path3_ans):

        #adding while statement if user inputs wrong directions, we can continue
        while True:

            self.choice1 = input("You begin your journey, but you shortly after you arrive at crossroad. would you like to go 'Left' or 'Right'? ").lower()

            if self.choice1 not in path1:
                print('Invalid direction, please try again.')
                continue

            if self.choice1 != path1_ans:
                print("You fell in to a hole. Game Over.")
                
                return None
            
            #we used for readability
            break

        print("Nice!")
        self.path2_journey(path2, path2_ans, path3, path3_ans)

    def path2_journey(self, path2, path2_ans, path3, path3_ans):
        
        while True:
            self.choice2 = input("You arrive at a small river. The island is just in the middle. You can 'Build' a boat or 'Swim' across. What would you like to do? ").lower()

            if self.choice2 not in path2:
                print('Invalid input, please try again.')
                continue

            if self.choice2 != path2_ans:

                if self.choice2 == 'build':
                    print("Oops, your boat had holes in it, and you drowned. Game Over.")
                else:
                    print("Oops, you ran out of breath and drowned. Game Over.")

                return None
            
            break

        print("Good Job!")
        self.path3_journey(path3, path3_ans)


    def path3_journey(self, path3, path3_ans):

        while True:
            self.choice3 = input("You go upto tower in the island. You see three different colored doors. 'Red', 'Blue' & 'Yellow'. You decide to go into one. ").lower()

            if self.choice3 not in path3:
                print('Invalid choice, please try again.')
                continue

            if self.choice3 != path3_ans:

                if self.choice3 == 'red':
                    print("Game Over. The room was full of lava.")
                elif self.choice3 == 'yellow':
                    print("Game OVer. The room was full of bioharzard radioactive chemicals.")
                else:
                    print("Game Over. You fell down a river of cyanide.")

                return None
            
            break

        self.win = True
        return None

        


player1 = Path()

player1.path1_journey(path1, path1_ans, path2, path2_ans, path3, path3_ans)


if player1.win == False:
    
    print("Try again.")
else:
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("Congrats! You found the treasure.")