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