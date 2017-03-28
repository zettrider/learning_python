'''
II. Create an IP address converter (dotted decimal to binary):

    A. Prompt a user for an IP address in dotted decimal format.

    B. Convert this IP address to binary and display the binary result on the screen (a binary string for each octet).

    Example output:
    first_octet    second_octet     third_octet    fourth_octet
    0b1010        0b1011000        0b1010         0b10011
'''

network_raw = input("Please enter a valid IPv4 Address to convert it to binary:\n")

network_list = network_raw.split(".")

print("%20s %20s %20s %20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet"))

for i in range (0, len(network_list)):
    #print(network_list[i])
    octet = bin(int(network_list[i]))
    print("%20s" %octet, end="" )