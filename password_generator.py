from random import randint as randint
"""
Generates A Strong Password with given number of letters symbols and numbers. 
"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= 10 
nr_symbols = 3
nr_numbers = 2
def generate_password():
    def random_picker(number,listOfChar) -> list:
        """
        picks a random sublist from "listOfChar" of length "number"
        """
        temp_list_char =[]
        for i in range(number):
            random_number = randint(0, len(listOfChar)-1)
            temp_list_char.append(listOfChar[random_number])
        return temp_list_char

    def jumbler(listOfChar) -> list:
        """
        jumbles the given list with a new order
        """
        tempList = []
        for i in range(len(listOfChar)):

            # randomly takes a char from the list and adds it to a temporary list and then removes it from the original list
            random_number = randint(0, len(listOfChar)-1)
            tempList.append(listOfChar[random_number])
            listOfChar.remove(listOfChar[random_number])
        return tempList

    # Extracting random characters
    random_letters = random_picker(nr_letters,letters)
    random_numbers = random_picker(nr_numbers,numbers)
    random_symbols = random_picker(nr_symbols,symbols)

    #Combining extracted characters into a single list
    random_letters.extend(random_numbers)
    random_letters.extend(random_symbols)

    # Shuffling the list to a random order
    password_letters = jumbler(random_letters)

    #Converting the list of strings to a single string (password)
    password = ""
    for i in password_letters:
        password = password + i
        


    return password
