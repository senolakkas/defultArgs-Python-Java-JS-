####Python
def f(a, b=10, c=20, *args, **kargs):
    d = args[2] if len(args)>2 else 40
    # if key "x" exists in kargs dict returns its value (kargs["x"]), otherwise returns default value 40
    e = kargs.get("x",50)
    print("a={}, b={}, c={}, d={}, e={}".format(a,b,c,d,e))
    #
print f(1,2)
print f(1,2,3,4)
print f(1,2,3,4,5,x="x")
print f(1,2,3,4,5,6,7)
