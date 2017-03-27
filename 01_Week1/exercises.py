'''
Task 1:

1. Use the split method to divide the following IPv6 address into groups of 4 hex digits (i.e. split on the ":")
FE80:0000:0000:0000:0101:A3EF:EE1E:1719

Other possible Solution:
ipv6Sections = ipv6.split(":")
print(ipv6Sections)
'''

ipv6 = input("Please enter valid IPv6 Address to split:\n")
if ipv6 == "":
    ipv6 = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"
ipv6Split = str.split(ipv6,":")
print(ipv6Split)


'''
Task 2:

2. Use the join method to reunite your split IPv6 address back to its original value.

'''

print(":".join(ipv6Split))

'''
Task 3:

3. In the test3.py script above, how would you modify this to remove the trailing newline on the end of 192.168.1.1?
'''

test3 = "192.168.1.1\n"
for item in test3:
    item.strip()
    print(item,end="")

