"""

A text based resource management game. There is no pressure to min-max this is meant to be relaxing. 
~Enjoy

Author: Louis Lu || Date: 12/11/2020
"""

flag = 0
scene = 0

def move():
    if (flag==0):
        opening_text = "\nAdventurer, your decision in movement is of the utmost importance!\n"
        opening_text+= "Please let me know when you have decided so that I may go back to my family..."
        opening_text+= "it has been several years since the last adventurer made a move, and I am weary."
        opening_text+= " My bones have long grown tired and my soul desperately wishes to sleep..."
        opening_text+= "\n\nGrant an old soul their last wish? (Enter North, East, South, West)"
    print(opening_text)
    direction = input()
    direction=direction.lower()
    if (direction == "north"):
        print("joy")
    elif (direction == "east"):
        print("joy")
    elif (direction == "south"):
        print("joy")
    elif (direction == "west"):
        print("joy")
    elif (direction == "no"):
        if (scene==0):
            scene_text = "The last adventurer said the same thing but I've learned since then..."
            scene_text+= "\nNone of you can be trusted so I've come up with a few tricks just in case."
            scene_text+= "\n\n You Died"

def print_current_state(current_state):
    print('-'*22)
    state_size = len(current_state)
    for rows in range(state_size):
        for cols in range(state_size):
            if (cols==0):
                print('|', end='')
            print(current_state[rows][cols], sep=' ', end= ' ')
            if (cols==2 or cols==5):
                print('|', end = '')
        print('|')
        if (rows==2 or rows==5):
            print('-'*22)
    print('-'*22)
    
#Print out the start state of the map
current_state = [ [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  [ '.', '.', '.', '.', '.', '.', '.', '.', '.'] ]

print_current_state(current_state)
move()