while True:
    a = [1,2,3,4,5,6,7]
    b = int(input("numero: "))
    c = []
    if b in a:
        c.append(b)
        print("existe: %d"%b)
    if b == 99:
        break
    
    
