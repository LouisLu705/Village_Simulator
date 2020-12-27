"""

A text based resource management game. There is no pressure to min-max this is meant to be relaxing. 
~Enjoy

Author: Louis Lu || Date: 12/11/2020
"""

import random

class Player:
    def __init__(self):
    # Create a new character    
        self.health = (random.randint(0,20))
        self.attack = (random.randint(0,20))
        self.luck = (random.randint(0,20))
        self.defense = (random.randint(0,20))
        self.speed = (random.randint(0,20))
            
        
    def move(self, board):
        print_bd = True
        while (True):
            if (print_bd):
                board.print_current_state()
            print_bd = True
            print("\nPlease enter a direction: (North, East, South, West)")
            direction = input()
            lowercase_dir = direction.lower()
            if (lowercase_dir == "north"):
                board.current_state[board.y][board.x]='.'
                board.y=board.y-1
            elif (lowercase_dir == "east"):
                board.current_state[board.y][board.x]='.'
                board.x=board.x-1
            elif (lowercase_dir == "south"):
                board.current_state[board.y][board.x]='.'
                board.y=board.y+1
            elif (lowercase_dir == "west"):
                board.current_state[board.y][board.x]='.'
                board.x=board.x+1
            elif (lowercase_dir == "exit"):
                break
            else:
                print("unknown direction \'{}\' entered".format(direction))
                print_bd = False
            board.current_state[board.y][board.x]='P'
                            
class Board:
    def __init__(self):
        self.current_state=[ [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                             [ '.', '.', '.', '.', '.', '.', '.', '.', '.'] ] 
        self.x = random.randint(0,8)
        self.y = random.randint(0,8)
        
        #Note the first element in a 2d list represents the "row" so the first "[]" 
        #is the y position in the board state.
        self.current_state[self.y][self.x]='P'
        
        
    def print_current_state(self):
        print('-'*22)
        state_size = len(self.current_state)
        for rows in range(state_size):
            for cols in range(state_size):
                if (cols==0):
                    print('|', end='')
                print(self.current_state[rows][cols], sep=' ', end= ' ')
                if (cols==2 or cols==5):
                    print('|', end = '')
            print('|')
            if (rows==2 or rows==5):
                print('-'*22)
        print('-'*22)

def start():
    """
    Start the introduction text to introduce the basics of the game to the player
    """
    name = '\x1b[36m' + "Village Simulator" + '\x1b[0m'
    print("Welcome to {}!".format(name),end = "\n\n")
    
    print("The smog clouds slowly drift up into the air as you stare aimlessly at the night sky. "  
          "Like clockwork the factory doesn't stop. Loud sounds continue to ring out "
          "from within the compound as you reminisce about where you spent your youth."
          "Time doesn't stop for anyone and slowly all the people you once knew left. Finally your time has come. "
          "With that you step away from the doors and leave without looking back. ",end="\n\n")
    
    print("A few months pass and you find yourself in the middle of an Australian forest. "
          "The air is clean and outside the sun is shining. The sun illuminates your slightly "
          "disheveled face but plastered on is an undeniable smile. You've never felt more relaxed "
          "and now you have finally sealed the deal. This land is yours and you are free to build it up "
          "into what you've always dreamed of.",end="\n\n")
    
    print("As you begin thinking about the future a bright light suddenly appears in front of you. "
          "In a flash you are consumed by the light and mere moments later find yourself sitting on the "
          "ground of an unfamiliar land. Looking up into the sky you see 3 suns and a roar sounds out as "
          "a massive dragon seems to have just flown by overhead. Confused and lost you remember the last words " 
          "the person who sold this land to you said. \"Good luck\" You stand up and ponder briefly about whether "
          "he knew all along. Seeing as you may never know the truth a level of grim determination you didn't know you were capable of "
          "fills you as you take your first steps towards a firmer future. Although you didn't know it this is the beginning "
          "of how this world would change forever...")
    
    
    
def main():
    # print out start() text to introduce the player to the setting
    start()  
    
    # board and player object for the rest of the instance
    bd_state = Board()
    Character = Player()
        
    
    while (True):
        cmd=input()
        
        if (cmd == "exit"):
            break
        elif (cmd == "move"):
            Character.move(bd_state)
        
        
"""
Beginning driver code
"""
flag = 0
scene = 0
main()