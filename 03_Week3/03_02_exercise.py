'''
II. Modify the 'show ip bgp' exercise from class2.   Simplify the program using the flow-control 
statements from this class.

Untouched since flow control already in place.
'''

entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

entry_combined = [entry1, entry2, entry3, entry4]

print("%-20s %s" % ("ip_prefix", "as_path"))

for item in entry_combined:

    entry_list = (str.split(item))

    ip_prefix = (entry_list[1])
    as_path = (entry_list[4:len(entry_list)-1])

    print("%-20s %s" % (ip_prefix, as_path))
