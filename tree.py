
for t in range(0,3):
    for x in range(0,7):
        for y in range(0,14):
            if (y < (7 - x) or (y > 7 + x)):
                print(" ", end ='')
            else:
                print("*", end = '')
        
        print(" ")

for s in range(0,4):
    for r in range(0,14):
        if ((r < 6) or (r > 8)):
            print(" ", end='')
        else:
            print("*", end='')
    
    print("")
            
