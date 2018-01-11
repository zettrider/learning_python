"""
IV. Create a script that checks the validity of an IP address.  The IP address should be supplied on the command line.
    A. Check that the IP address contains 4 octets.
    B. The first octet must be between 1 - 223.
    C. The first octet cannot be 127.
    D. The IP address cannot be in the 169.254.X.X address space.
    E. The last three octets must range between 0 - 255.

    For output, print the IP and whether it is valid or not.
"""

import sys


def ip_validator(network_raw):
    network_list = network_raw.split(".")

    if (len(network_list)) == 4 \
            and 0 < (int(network_list[1])) <= 223 \
            and (int(network_list[0]) != 127
                 or (int(network_list[0] != 169) and int(network_list[1] != 254))) \
            and 0 <= (int(network_list[1])) <= 255 \
            and 0 <= (int(network_list[2])) <= 255 \
            and 0 <= (int(network_list[3])) <= 255 :
        print('%s is valid' % sys.argv)
    else:
        print('%s is NOT valid' % sys.argv)

if len(sys.argv) > 2:
    print('%s is NOT valid' % sys.argv)
elif len(sys.argv) < 2:
    print('%s is NOT valid' % sys.argv)
else:
    ip_validator(sys.argv[1])
