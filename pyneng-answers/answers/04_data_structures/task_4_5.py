# -*- coding: utf-8 -*-
"""
Task 4.5

From the strings command1 and command2, get a list of VLANs that exist
in both command1 and command2 (intersection).

In this case, the result should be a list: ['1', '3', '8']

Write the resulting list to the result variable.
(this is the variable that will be checked in the test)

Print the result list to the standard output (stdout) using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = command1.split()[-1].split(",")
vlans2 = command2.split()[-1].split(",")


result = sorted(set(vlans1) & set(vlans2))
result1 = sorted(set(vlans1).intersection(set(vlans2)))

print("使用& :" , result)
print("使用intersection :" , result1)
