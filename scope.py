x = 100    #global scope
def var():
    x = 90   #local scope
    print(x)
var()      
print(x)