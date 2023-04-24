txt = "hello, world!"
print(txt.find("w"))  # "w" -> 7 index in txt

txt = "hello, world!"
print(len(txt))  # 13 characters in txt -> hello, world!

txt = "hello, world!"
print(txt.capitalize())  # hello, world! -> Hello, world!

txt = "HELLO, WORLD!"
print(txt.lower())  # HELLO, WORLD! -> hello, world!

txt = "hello, world!"
print(txt.upper())  # hello, world! -> HELLO, WORLD!

txt = "hello, world!"
print(txt.isdigit())  # False

txt = "hello world"
print(txt.isalpha())  # False, but helloworld -> True

txt = "hello world"
print(txt.replace("world", "Python"))  # hello world -> hello Python

txt = "hello world"
print(txt.count("o"))  # 2 -> (o) is two times in txt -> hell(o) w(o)rld

txt = "hello world"
print(txt * 3, )  # hello worldhello worldhello world
