# To create a tic tac toe game in python i need:
# 1) Visual Representation - User Input - Funcrtion - Updates - New Visual
# - Display something visual to the user
# - Let the user update through an interaction
# - Update variables in the program
# - Display updated visual

# Displaying Information:


print([1,2,3])



print([1,2,3])
print([4,5,6])
print([7,8,9])


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)



row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']


display(row1,row2,row3)



row2[1] = 'X'



display(row1,row2,row3)


# Accepting User Input



input("Please enter a value: ")



result = input("Please enter a value: ")


result


result = input("Enter Value: ")


result_int = int(result)


position_index = int(input("Choose an index position: "))



type(position_index)



row2[position_index]


result = input("Enter a number: ")


2+2



input("Enter Number: ")



20+20


# Validating User Input

def user_choice():
    
    choice = 'WRONG'
    
    while choice.isdigit() == False:
        
    
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
    
    return int(choice)


user_choice()


result = 'WRONG VALUE'


acceptable_values = [0,1,2]


result in acceptable_values


result not in acceptable_values



def user_choice():
    
    # VARIABLES
    
    # Initial
    choice = 'WRONG'
    acceptable_range = range(0,11)
    within_range = False
    
    # TWO CONDITIONS TO CHECK
    #DIGIT OR WITHIN_RANGE==False
    
    while choice.isdigit() == False or within_range==False:
        
    
        choice = input("Please enter a number (0-10): ")
        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
            #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                    within_range = True
            else:
                print("Sorry, you are out of acceptable range 0-10)")
                within_range = False
    
    return int(choice)



user_choice()


game_list = [0,1,2]


def display_game(game_list):
    print("Here is the current list")
    print(game_list)


display_game(game_list)


def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")
            
    return int(choice)


position_choice()


def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list


replacement_choice(game_list,1)



def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        
        choice = input("Pick a position (Y or N): ")
        
        if choice not in ['Y','N']:
            print("Sorry, I dont understant, please choose Y or N ")
            
    if choice == "Y":
        return True
    else:
        return False


gameon_choice()



game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()