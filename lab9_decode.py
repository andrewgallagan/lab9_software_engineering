# Lab 9, Software Engineering: 'Decode' author: Andrew Gallagan
def decode(password):
    decoded_pass = ""
    sub_by = 0
    factor = 1

    # Get Factor to Subtract By
    for i in range(len(password)):
        sub_by += 3 * factor
        factor *= 10

    # Subtract by Factor
    # print("Sub By:", sub_by)
    decoded_pass = str(int(password) - int(sub_by))

    # Adds zeroes to fill front blank spaces during substraction, if lens don't match
    while(len(password) != len(decoded_pass)):
        decoded_pass = "0" + decoded_pass

    return decoded_pass