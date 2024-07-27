def decode(password):
    decoded = ""
    for i in password:
        num = int(i)
        num2 = (num - 3) % 10
        decoded += str(num2)
    return decoded