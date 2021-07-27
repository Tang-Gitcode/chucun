# 测试使用字符串
"""
%是格式化字符串，将格式化变量放到字符串中，在紧跟一个%，再紧跟着变量名即可

"""
x = "The are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)
print(x)
print(y)

print("i said: %r." % x)
print("i also said: '%s' ." % y)


hilarious = False
joke_evalution = "Isn't that joke so funny?! %r"

print(joke_evalution % hilarious)

w = "This is the left side of ..."
e = "a string with a right side ."

print(w + e)
