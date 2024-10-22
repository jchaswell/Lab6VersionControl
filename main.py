#Encode/Decode program

#Encoder, receives str of numbers of any length, returns int where each digit has been increased by three.
def encode(input_num):
    encoded_num = ''
    new_digit = 0
    for digit in str(input_num):
        encoded_digit = int(digit) + 3
        encoded_num += str(encoded_digit)[-1]
    return int(encoded_num)



def main():

    while True:
        menu_selection = int((input('Input 1 to enter a value, input 2 to decode value, 3 to exit: ')))
        #could add error checking to confirm 8 digit string of only nums
        if menu_selection == 1:
            input_num = int(input('Enter a number: '))
            encoded_num = encode(input_num)
            print(f'Your encoded number is: {encoded_num}')
            print()
        if menu_selection == 2:
            #TODO: call decode function here
            pass
        if menu_selection == 3:
            break

main()