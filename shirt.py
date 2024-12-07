RS = int(input("Enter number of red shirts: "))
BS = int(input("Enter number of blue shirts: "))
WS = int(input("Enter number of white shirts: "))

total = RS+BS+WS

proba = BS/total
probb = RS/total

probbga = probb
probaofb = proba * probb

print("probability")
print(round((probbga),3))

print("probability")
print(round((probaofb),3))