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

if len(sys.argv) > 2:
    print('%s is not valid' % sys.argv)
elif len(sys.argv) < 2:
    print('%s is not valid' % sys.argv)
else:
    network_raw = sys.argv[1]

    network_list = network_raw.split(".")

    if (len(network_list)) == 4 \
            and int(network_list[0]) >= 0 \
            and int(network_list[0]) <=223 \
            and (int(network_list[0]) != 127
                 or (int(network_list[0] != 169) and int(network_list[1] != 254))) \
            and 0 <= (int(network_list[1])) <= 255 \
            and 0 <= (int(network_list[2])) <= 255 \
            and 0 <= (int(network_list[3])) <= 255 :
            #and (for i in range (1,4):
            #    0 <= (int(network_list[i]) <= 255)):
        print('%s is valid' % sys.argv)
    else:
        print('not_valid')

#print(network_list[0:2])
#print(network_list)

#print(0 < (int(network_list[1]) < 255))


'''
for i in range (1,4):
    print(i)
    print(network_list[i])
    print(0 <= (int(network_list[i])) <= 255)
'''

'''
Test
'''

'''
Test2
'''
