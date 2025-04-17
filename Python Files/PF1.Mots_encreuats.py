def is_valid_word(wordlist, word):
    '''(lst of str, str) -> bool
    
    Return True if and only if word is an elementy wordlist.
    '''
    valid = False

    for w1 in worldlist:
        if w1 == word:
            valid = True
        
    return valid

def make_str_from(board, row_index):
    '''(list of list of str, int) -> str
    
    Return the characters from the row of the board with index row_index
    as a single string.
    '''
    
    row= ''
    
    for j in range(len(board(row_index))):
        row = row + board[row_index][j]
                   
    return row

def make_str_from_column(board, column_index):
    '''
    
    Return the characters from the column of the board with index row_column
    '''
    
    column= ''
    
    for i in range(len(borad)):
        column = column + board[i][column_index]
        
    return column
    

def board_contains_word_in_column(board, word):
    '''
    
    '''
    
    for i in range(len(board)):
        
        for column_index in range(len(board[i])):
            return True
        
    return False
        
    
    
def board_contains_word_in_column():
    '''
    
    '''
    
    for i in range(len(board)):
        
                                  
                                  
def board_contains_word():
    '''
    
    '''
    
    if board_contains_word



    
lenword= len(word)
if lenword >= 10:
    return lenword*3

elif (lenword >= 7 and lenword <=9):
    return lenword*2
    
    
def update_score(player_info, word):
    '''
    
    '''
    player_info[1] = player_info[1] + word_score(word)
    





def num_word_on_board(board, words):
    '''
    
    '''
    
    count= 0
    
    for i in words:
        if board_contains_word(board,i)
        
def read_words(words_file):
    '''
    
    '''
    
    list_words= []
    
    for line in words_file:
        list_words.append(line.rstrip('\n'))
        
    return list_words


words_file= open("wordlist.txt", "r")
print(read_words(word_file))


def read_board():
    '''
    one row of the board per line. Newlines are not included in the board
    '''
    
    for line in board_file:
        board2 =[]
        
        for item in line.rstrip('\n'):
            board2.append(item)
        board.append(board2)
        
    return board

board_file= open("board1.txt", "r")
print(read_board(board_file))
