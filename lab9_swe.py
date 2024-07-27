from lab9_decode import decode

# Lab 9, Software Engineering: 'Encode' author: Andrew Gallagan
def encode(password):
    encoded_pass = ""
    add_by = 0
    factor = 1

    # Get Factor to Add By (to "Encode" with)
    for i in range(len(password)):
        add_by += 3 * factor
        factor *= 10

    # Add by Factor
    # print("Add By:", add_by)
    encoded_pass = str(int(password) + int(add_by))

    # Adds zeroes to fill front blank spaces during substraction, if lens don't match
    while(len(password) != len(encoded_pass)):
        encoded_pass = "0" + encoded_pass

    return encoded_pass

###############################
# Insert Decode Function Here #
###############################

if __name__ == '__main__':

    # # Test 1
    # test_password = "12345555"
    # e_pass = encode(test_password)
    # print(e_pass)

    # d_pass = decode(e_pass)
    # print(d_pass)

    # # Test 2
    # test_password1 = "00009962"
    # e_pass1 = encode(test_password1)
    # print(e_pass1)

    # d_pass1 = decode(e_pass1)
    # print(d_pass1)

    quit = False
    e_pas = ""
    d_pas = ""
    print("Menu")
    print("-----------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    while(quit != True):
        option = input("\nPlease enter an option: ")

        if option == "1":
            try:
                p_enc = input("Please enter your password to encode: ")
                e_pas = encode(p_enc)
                print("Your password has been encoded and stored!")
            except:
                print("Something went wrong. Please try again.")

        if option == "2":
            try:
                d_pas = decode(e_pas)
                print("The encoded password is", e_pas, "and the original password is",d_pas, end="")
                print(".")
            except:
                print("Something went wrong. Please try again.")

        if option == "3":
            quit = True

        print("\nMenu")
        print("-----------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
