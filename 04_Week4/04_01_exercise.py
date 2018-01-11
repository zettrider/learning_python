"""
Prompt a user to input an IP address.  Re-using some of the code from class3, exercise4--determine if the IP address
is valid.  Continue prompting the user to re-input an IP address until a valid IP address is input.
"""

not_done = True

while not_done is True:
    ip_network = input("\n\nEnter a network number: ")

    network_list = ip_network.split(".")

    valid_ip = False

    if (len(network_list)) == 4 \
            and 0 < (int(network_list[1])) <= 223 \
            and (int(network_list[0]) != 127
                 or (int(network_list[0] != 169) and int(network_list[1] != 254))) \
            and 0 <= (int(network_list[1])) <= 255 \
            and 0 <= (int(network_list[2])) <= 255 \
            and 0 <= (int(network_list[3])) <= 255:
        valid_ip = True

    if valid_ip is True:
        not_done = False
    else:
        print('%s is NOT valid - please try again' % ip_network)

print('%s is valid' % ip_network)