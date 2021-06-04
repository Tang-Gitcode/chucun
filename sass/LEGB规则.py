#测试LEDG规则


print(str(30))
#str = "global str"
def outer():

    #str = "outer"
    def inner():
        #str = "inner"
        print(str)
    inner()

outer()