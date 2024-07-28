# Lab 9, Software Engineering: Decode (Notional) Prior to Peer-Update
#        (Please replace with your implementation below: )

def encode(password):
    encoded_password = ""
    for digit in password:
        # math for each digit to encode
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password
