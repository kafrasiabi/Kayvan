(input('Pick a number between 0 and 100, ready?')) #press enter to begin
num_of_guesses = 0 #guess counter
low_bound = 0
high_bound = 100
guess = int(round((high_bound + low_bound)/2)) #guesses are rounded to nearest whole number, take the half of the low to hind bounds
num_confirm_flag = False #flag that will break while loop, non-ambiguous names replaced
while num_confirm_flag is False: 
    num_confirm_prompt = input('Is your number ' + str(guess) + '? (y/n): ')
    if num_confirm_prompt == 'n' or num_confirm_prompt == 'N': #includes both options for input
        less_or_more_flag = False
        while less_or_more_flag is False:
            less_or_more_prompt = input('Is it less than or more than ' + str(guess) + '? (l/m): ')
            if less_or_more_prompt == 'l':
                high_bound = guess
                less_or_more_flag = True
            elif less_or_more_prompt == 'm':
                low_bound = guess
                less_or_more_flag = True
            else:
                print('Invalid input, try again.') #I want this statement to go back to line 11, not line 9 
    elif num_confirm_prompt == 'y':
        num_confirm_flag = True #ends the while loop, wanted to use break, but then I wouldn't have a statement to use while loop continuously, help?
    else:
        print('Invalid input, try again.')
        num_of_guesses -= 1 #reduces guess count so that invalid inputs don't count
    num_of_guesses += 1
    guess = round((high_bound + low_bound)/2)
if num_of_guesses == 1:
    t = "try" #grammar
else:
    t = "tries"
print("Hurray! I guessed your number was " + str(guess) + " in " + str(num_of_guesses) + " " + str(t) + "!")

