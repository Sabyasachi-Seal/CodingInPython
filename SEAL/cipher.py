import random
def encode(x,y):
    for letter in x:
        new_l = chr(ord(letter)+y)
        print(new_l if 97<=ord(new_l)<=122 or 65<=ord(new_l)<=90 else chr(ord(letter)-(26-y)), end="")


def decode(x, y, spc):
    for letter in x:
        new_l = chr(ord(letter)-y)
        print(new_l if 97<=ord(new_l)<=122 or 65<=ord(new_l)<=90 else chr(ord(letter)+(26-y)), end="") if letter not in spc else print(" ", end="")


choice, spc = input("Encode(0) or Decode(1)? :"), ["&", "*", "^", "%", "@"]
x1, y= input("Enter input: "), int(input("Enter Key: "))
x = x1.replace(" ", random.choice(spc))
print(x)
encode(x, y) if choice=="0" else decode(x, y, spc)
