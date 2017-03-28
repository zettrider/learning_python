"""
IV. You have the following string from "show version" on a Cisco router

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

Note, the string is a single line; there is no newline in the string.

How would you process this string to retrieve only the IOS version:

   ios_version = "15.0(1)M4"


Try to make it generic (i.e. assume that the IOS version can change).

You can assume that the commas divide this string into four sections and
that the string will always have 'Cisco IOS Software', 'Version', and 'RELEASE SOFTWARE' in it.
"""

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

divided_ios = cisco_ios.split(sep=",")

for i in range(0, len(divided_ios)):
    if divided_ios[i].strip().startswith("Version"):
        divided_version = divided_ios[i].split(sep=" ")
        print('ios_version = "%s"' % divided_version[2])