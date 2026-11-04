def xor_division(dividend, divisor):
    dividend = list(dividend)
    n = len(divisor)

    for i in range(len(dividend) - n + 1):
        if dividend[i] == '1':
            for j in range(n):
                dividend[i + j] = str(
                    int(dividend[i + j]) ^ int(divisor[j])
                )

    return ''.join(dividend[-(n - 1):])


msg = input("Enter the binary message: ")
gen = input("Enter the generator polynomial: ")

# Sender side
padded_msg = msg + '0' * (len(gen) - 1)

remainder = xor_division(padded_msg, gen)

print("Sender Side:")
print("Padded Message:", padded_msg)
print("CRC Remainder:", remainder)

transmitted_msg = msg + remainder
print("Transmitted Message:", transmitted_msg)

# Receiver side
print("\nReceiver Side:")
print("Received Message:", transmitted_msg)

receiver_remainder = xor_division(transmitted_msg, gen)

print("Receiver Remainder:", receiver_remainder)

if int(receiver_remainder, 2) == 0:
    print("Message received correctly. No error detected.")
else:
    print("Error detected in received message.")
