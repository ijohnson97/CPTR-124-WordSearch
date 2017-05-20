##  Name: Ian Johnson
##  Assignment Number: 
##  Assignment: Word Search
##  Date last modified: 09 November, 2016
## Honor statement: I have neither given nor received any unauthorized help on this assignment.

from random import *

gridSize = 20        ## Allows the size of the grid to be changed for test purposes

words = []        ## This list will contain words from the text file
grid = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]       ## This list will contian each line of the block, as a list
ansGrid = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
seq = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

## Import words
with open('ListOfWords.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')        ## Remove new line character
        words.append(line)               ## Add words to list


def initialize_grids():
    global grid, ansGrid
    ## Create random grid of letters
    for i in range(gridSize):
        for n in range(gridSize):
            letter = choice(seq)
            grid[i].append(letter)
        grid[i].append('\n')
    
    for i in range(gridSize):
        for n in range(gridSize):
            ansGrid[i].append('.')
        ansGrid[i].append('\n')


## Function for adding words
def place_word(word):
    global grid, ansGrid
    '''
    Randomly chooses one of the six possible orientations:
        0. Horizontal
        1. Vertical
        2. Diagonal
        3. Horizontal Backwards
        4. Vertical Backwards
        5. Diagonal Backwards
    '''
    orientation = randrange(0,6)
    
    ## Horizontal
    if orientation == 0:
        while True:
            fits = True
            k = randrange(gridSize)     ## Choose a row
            j = randrange(gridSize - len(word))    ## Choose a column
            i = 0

            for char in word:
                if ansGrid[k][j + i] == '.' or ansGrid[k][j + i] == char:
                    i += 1
                else:
                    fits = False
                    break
            if fits:
                for char in word:
                    ansGrid[k][j] = char
                    grid[k][j] = char
                    j += 1
                return
    
    ## Veritcal
    elif orientation == 1:
        while True:
            fits = True
            k = randrange(gridSize - len(word))     ## Choose a row
            j = randrange(gridSize)    ## Choose a column
            i = 0
            
            for char in word:
                if ansGrid[k + i][j] == '.' or ansGrid[k + i][j] == char:
                    i += 1
                else:
                    fits = False
                    break
            if fits:
                for char in word:
                    ansGrid[k][j] = char
                    grid[k][j] = char
                    k += 1
                return
            
    ## Diagonal
    elif orientation == 2:
        while True:
            fits = True
            k = randrange(gridSize - len(word))    ## Choose a row
            j = randrange(gridSize - len(word))    ## Choose a column
            i = 0
            
            for char in word:
                if ansGrid[k + i][j + i] == '.' or ansGrid[k + i][j + i] == char:
                    i += 1
                else:
                    fits = False
                    break
            if fits:
                for char in word:
                    ansGrid[k][j] = char
                    grid[k][j] = char
                    k += 1
                    j += 1
                return
            
    ## Horizontal Backwards
    elif orientation == 3:
        while True:
            fits = True
            k = randrange(gridSize)     ## Choose a row
            j = randrange(len(word), gridSize)    ## Choose a column
            i = 0

            for char in word:
                if ansGrid[k][j + i] == '.' or ansGrid[k][j + i] == char:
                    i -= 1
                else:
                    fits = False
                    break
            if fits:
                for char in word:
                    ansGrid[k][j] = char
                    grid[k][j] = char
                    j -= 1
                return
        
    ## Vertical Backwards
    elif orientation == 4:
        while True:
            fits = True
            k = randrange(len(word), gridSize)    ## Choose a row
            j = randrange(gridSize)        ## Choose a column
            i = 0
            
            for char in word:
                if ansGrid[k + i][j] == '.' or ansGrid[k + i][j] == char:
                    i -= 1
                else:
                    fits = False
                    break
            if fits:
                for char in word:
                    ansGrid[k][j] = char
                    grid[k][j] = char
                    k -= 1
                return
            
    ## Diagonal Backwards
    elif orientation == 5:
        while True:
            fits = True
            k = randrange(len(word), gridSize)    ## Choose a row
            j = randrange(len(word), gridSize)    ## Choose a column
            i = 0
            
            for char in word:
                if ansGrid[k + i][j + i] == '.' or ansGrid[k + i][j + i] == char:
                    i -= 1
                else:
                    fits = False
                    break
            if fits:
                for char in word:
                    ansGrid[k][j] = char
                    grid[k][j] = char
                    k -= 1
                    j -= 1
                return

## Print Grid
def print_grid():
    print('Word Search')
    for i in range(len(grid)):
        for n in grid[i]:
            print(n, end=' ')
    
    print(' ')
    
    for word in words:
        print(word, end=' ')
    print('\n')


def print_ansGrid():
    print('*******************************\nAnswer Key:')
    for i in range(len(ansGrid)):
        for n in ansGrid[i]:
            print(n, end=' ')
    print('*******************************')
    
initialize_grids()

## Uses the palce_word() function to add words to grid
for word in words:
    place_word(word)
print_grid()
print_ansGrid()