#Encode/Decode program

#Encoder, receives str of numbers of any length, returns int where each digit has been increased by three.
def encode(input_num):
    encoded_num = ''
    for digit in str(input_num):
        encoded_digit = (int(digit) + 3) % 10
        encoded_num += str(encoded_digit)
    return int(encoded_num)

#decoder will take the encoded str and return the original password
def decode(encoded_num):
    decoded_num = ''
    for digit in str(encoded_num): #iterate through each num in str and subtract 3
        decoded_digit = (int(digit) - 3) % 10 #use % to compensate for negative values
        decoded_num += str(decoded_digit)
    return decoded_num



#set up main function menu screen
def main():
    encoded_num = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        #user will select an option from menu
        try:
            menu_option = int(input("Please enter an option: "))
        except ValueError:
            print("Invalid input") #qc for bugs if user selects invalid option #
            continue

        #allow user to enter password they wish to encode
        if menu_option == 1:
            input_num = (input("Please enter your password to encode:  "))
            if len(input_num) == 8 and input_num.isdigit(): #password should be 8 characters long and all numbers
                encoded_num = encode(input_num)
                print(f"Your password has been encoded and stored!")
            else:
                print("Invalid input.") #qc for bugs if password not correct format
            print("")

        #print out the encoded password, as well as the original
        elif menu_option == 2:
            if encoded_num is not None:  #check if a password has been encoded
                original_password = decode(encoded_num)
                print(f"Then encoded password is {encoded_num}, the original password is {original_password}.")
            else:
                print("Please enter a valid password.") #qc if no original password entered
                print("")

        elif menu_option == 3:
            break
if __name__ == '__main__':
    main()