# Lab 9, Software Engineering: Decode (Notional) Prior to Peer-Update
#        (Please replace with your implementation below: )

def decode(encoded_pass):
    password = ""
    for i in encoded_pass:
        digit = int(i) - 3
        password += str(digit)
    return password
