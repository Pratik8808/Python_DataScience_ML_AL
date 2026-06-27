no=11   # global Variable
def Display():
    global no
    no=21
    print("From Display",no)

print("Before :",no)

Display()
print("After :",no)
    


