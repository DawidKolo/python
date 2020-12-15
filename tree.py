
for t in range(0,31):
    for x in range(0,7):
        for y in range(0,14):
            if (y < (7 - x) or (y > 7 + x)):
                print(" ", end ='')
            else:
                print("*", end = '')
        
        print(" ")
