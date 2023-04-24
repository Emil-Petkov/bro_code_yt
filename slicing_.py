# slicing = [start:end:step]

txt = "Hello, world!"
print(txt[::])  # Hello, world!
print(txt[:-1])  # Hello, world -> without (!)
print(txt[:3])  # Start to third element. At index 0 to index 2 -> Hel ("H" == index 0)("e" == index 1)("l" == index 2)
print(txt[:3 + 1])  # Start to 4th element, because is 3 + 1 or txt[:4] == "Hell" at index 0 to index 3
print(txt[::2])  # txt with step 2 - > "Hlo ol!"
print(txt[:])  # "Hello, world!"
print(txt[:-3])  # "Hello, wor"
print(txt[:-3:3])  # "Hl r"
print(txt[::-1])  # reverse txt -> "!dlrow ,olleH"
#############################################################################

website1 = "http://www.site_1.com"
website2 = "http://www.site_2.com"
slicing = slice(11, -4)

print(website1[slicing])  # slice object
print(website2[slicing])
