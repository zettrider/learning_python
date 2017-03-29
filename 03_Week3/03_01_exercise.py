"""
I. Create an IP address converter (dotted decimal to binary).  This will be similar to what we did in class2 except:

    A. Make the IP address a command-line argument instead of prompting the user for it.
        ./binary_converter.py 10.88.17.23

    B. Simplify the script logic by using the flow-control statements that we learned in this class.

    C. Zero-pad the digits such that the binary output is always 8-binary digits long.  
       Strip off the leading '0b' characters.  For example,

        OLD:     0b1010
        NEW:    00001010

    D. Print to standard output using a dotted binary format.  For example,

        IP address          Binary
      10.88.17.23          00001010.01011000.00010001.00010111
"""

import sys

if len(sys.argv) < 2:
    print("Please input valid IP address as argument.")
elif len (sys.argv) > 2:
    print("Please give one valid IP address as argument.")
else:
    network_raw = sys.argv[1]

    network_list = network_raw.split(".")
    octet_binary = []

    for i in range (0, len(network_list)):
        #print(network_list[i])
        octet = bin(int(network_list[i]))
        octet_binary.append(format(int(network_list[i]), '08b'))

    print("%-20s %s" % ("IP address", "Binary"))
    print("%-20s %s" % (sys.argv[1], ".".join(octet_binary)))
