#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f=cgi.FieldStorage()
t=f.getvalue("x")
if t == "1":
    print("""
    Vehicle Number = HR 26 DA 2330
    Vehicle Company = Maruti Suzuki
    Name of the owner = Vineet Sharma
    Registration Date = 12/06/2018
    Insurance = 18/09/2022
    State = Haryana
    Country = India
            """)
elif t == "2":
    print("""
    Vehicle Number = HR 26 D0 5551
    Vehicle Company = Maruti Suzuki
    Name of the owner = Akhilesh Verma
    Registration Date = 30/04/2019
    Insurance = 14/05/2021
    State = Haryana
    Country = India
        """)
else :
    print("Not Found")
