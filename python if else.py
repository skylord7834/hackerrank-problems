n=int(input("Enter n:"))
if (n%2!=0):
    print("Weired")
else:
    if n in range(2,6):
        print("Not Weired")
        
    elif n in range(6,21):
        print("Weired")
    
    elif n>20:
        print("Not Weired")