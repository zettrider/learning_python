'''

I. Create a script that does the following:

A.  Prompts the user to input an IP network.

    Notes:
    1. For simplicity the network is always assumed to be a /24 network
    2. The network can be entered in using one of the following three formats 10.88.17.0, 10.88.17., or 10.88.17

B.  Regardless of which of the three formats is used, store this IP network as a list in the following format
    ['10', '88', '17', '0'] i.e. a list with four octets (all strings), the last octet is always zero (a string).

C.  Print the IP network out to the screen.

D.  Print a table that looks like the following (columns 20 characters in width):

    NETWORK_NUMBER   FIRST_OCTET_BINARY      FIRST_OCTET_HEX
    88.19.107.0      0b1011000               0x58

'''

network_raw = input("Please enter the first three or all four IPv4 Address Segments:\n")

print("The Input is: %s" %network_raw)

network_list = network_raw.split(".")

if len(network_list) == 4:
    network_list[len(network_list)-1] = "0"
if len(network_list) == 3:
    network_list.append("0")

network_address = ".".join(network_list)
print("The network address is: %s" %network_address)

first_octet_binary = (bin(int(network_list[0])))

first_octet_hex = (hex(int(network_list[0])))

print("%20s %20s %20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX"))
print("%20s %20s %20s" % (network_address, first_octet_binary, first_octet_hex))