n1 = int(input("first number : "))
n2 = int(input("second number : "))
s1 = str(input("first word : "))
s2 = str(input("second word : "))
try:
    for i in range(1,100):
        if i % n1 == 0 and i % n2 == 0 :
            print(s1 + s2)
        elif i % n1 == 0 :
            print(s1)
        elif i % n2 == 0 :
            print(s2)
        else :
            print(i)
except:
    print("there is a probleme")
    

