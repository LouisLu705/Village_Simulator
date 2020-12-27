"""

A text based resource management game. There is no pressure to min-max this is meant to be relaxing. 
~Enjoy

Author: Louis Lu || Date: 12/11/2020
"""

import random
import sys

class Player:
    def __init__(self):
    # Create a new character    
        self.health = (random.randint(0,20))
        self.attack = (random.randint(0,20))
        self.luck = (random.randint(0,20))
        self.defense = (random.randint(0,20))
        self.speed = (random.randint(0,20))
            
        
    def move(self, board, all_boards):
        print_bd = True
        while (True):
            if (print_bd):
                board.print_current_state()
            print_bd = True
            print("\nPlease enter a direction: (North, East, South, West)")
            direction = input()
            lowercase_dir = direction.lower()
            if (lowercase_dir == "north" or lowercase_dir == 'n'):
                board.current_state[board.y][board.x]='.'
                board.y=board.y-1
            elif (lowercase_dir == "east" or lowercase_dir == 'e'):
                board.current_state[board.y][board.x]='.'
                board.x=board.x-1
            elif (lowercase_dir == "south" or lowercase_dir == 's'):
                board.current_state[board.y][board.x]='.'
                board.y=board.y+1
            elif (lowercase_dir == "west" or lowercase_dir == 'w'):
                board.current_state[board.y][board.x]='.'
                board.x=board.x+1
            elif (lowercase_dir == "exit"):
                sys.exit("Thank you for playing {}.".format(name))
            else:
                print("unknown direction \'{}\' entered".format(direction))
                print_bd = False
                
            global map_value, last_map_value
            old_x = board.x
            old_y = board.y
            #Let the even map_values hash to the bd_states which cross the x bounds
            #Let the odd map_values hash to the bd_states which cross the y bounds
            if (board.y < 0):
                if (map_value <= 1):
                    last_map_value = map_value
                    if (map_value < 0):
                        map_value=2*map_value-1
                    else:
                        map_value = -2*map_value-1
                    if (map_value in all_boards):
                        board = all_boards[map_value]
                        print("y1 is less than 0 with map_val: {}".format(map_value))
                    else:
                        board = Board()
                        board.current_state[board.y][board.x]='.'
                        all_boards[map_value]=board
                elif (map_value > last_map_value):
                    map_value = last_map_value
                    last_map_value = (map_value-1)/2
                    board = all_boards[map_value]
                    print("y2 is less than 0 with map_val: {}".format(map_value))
                board.y = 8
                board.x = old_x
            elif (board.y > 8):
                if (map_value >=1):
                    last_map_value = map_value
                    map_value=2*map_value+1
                    if (map_value in all_boards):
                        board = all_boards[map_value]
                        print("y3 is greater than 8 with map_val: {}".format(map_value))
                    else:
                        board = Board()
                        board.current_state[board.y][board.x]='.'
                        all_boards[map_value]=board
                elif (map_value < last_map_value):
                    map_value = last_map_value
                    if ((map_value+1)/2 == -1):
                        last_map_value = 1
                    else:
                        last_map_value = (last_map_value+1)/2
                    board = all_boards[map_value]
                    print("y4 is greater than 8 with map_val: {}".format(map_value))
                board.y = 0
                board.x = old_x
            elif (board.x < 0):
                if (map_value <=1):
                    last_map_value = map_value
                    if (map_value < 0):
                        map_value=2*map_value
                    else:
                        map_value=-2*map_value
                    if (map_value in all_boards):
                        board = all_boards[map_value]
                    else:
                        board = Board()
                        board.current_state[board.y][board.x]='.'
                        all_boards[map_value]=board
                elif (map_value > last_map_value):
                    map_value = last_map_value
                    last_map_value = map_value/2
                    board = all_boards[map_value]
                    #debug print statement
                    #print("x1 is less than 0 with map_val: {}".format(map_value))
                board.x = 8
                board.y = old_y
            elif (board.x > 8):
                if (map_value >= 1):
                    last_map_value = map_value
                    map_value=2*map_value
                    if (map_value in all_boards):
                        board = all_boards[map_value]
                    else:
                        board = Board()
                        board.current_state[board.y][board.x]='.'
                        all_boards[map_value]=board
                elif (map_value < last_map_value):
                    map_value = last_map_value
                    if (map_value/2 == -1):
                        last_map_value = 1
                    else:
                        last_map_value = last_map_value/2
                    board = all_boards[map_value]
                    #debug print statement
                    #print("x3 is greater than 8 with map_val: {}".format(map_value))
                    
                board.x = 0
                board.y = old_y
            board.current_state[board.y][board.x]='P'
            print(all_boards)
                            
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
        
        rng_range = random.randint(10,25)
        for rng in range(rng_range):
            rng_x = random.randint(0,8)
            rng_y = random.randint(0,8)
            if (rng_x == self.x and rng_y == self.y):
                continue
            else:
                self.current_state[rng_y][rng_x] = '^'
        
        
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
        
    all_boards = {}
    all_boards[map_value] = board

    
    while (True):
        cmd=input()
        
        if (cmd == "exit"):
            sys.exit("Thank you for playing {}.".format(name))
        elif (cmd == "move"):
            Character.move(board, all_boards)
   

"""
Global Variables
"""
flag = 0
scene = 0
map_value = 1  
name = '\x1b[36m' + "Village Simulator" + '\x1b[0m'
last_map_value = 1  
board = Board()
Character = Player() 
"""
Beginning driver code
"""
main()