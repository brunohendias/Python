n1 = float(input())
n2 = float(input())
n3 = float(input())
if n1 > n2 and n1> n3 and n2 < n3:
    print("o maior numero foi %.2f e o menor foi %.2f"%(n1, n2))
elif n1 > n2 and n1> n3 and n3 < n2:
    print("o maior numero foi %.2f e o menor foi %.2f"%(n1, n3))
elif n2 > n1 and n2 > n3 and n1 < n3:
    print("o maior numero foi %.2f e o menor foi %.2f"%(n2, n1))
elif n2 > n1 and n2 > n3 and n3 < n1:
    print("o maior numero foi %.2f e o menor foi %.2f"%(n2, n3))
elif n3 > n2 and n3 > n1 and n2 < n1:
    print("o maior numero foi %.2f e o menor foi %.2f"%(n3, n2))
elif n3 > n2 and n3 > n1 and n1 < n2:
    print("o maior numero foi %.2f e o menor foi %.2f"%(n3, n1))
