import sympy

def solve(a, b):
    s = sympy.fraction(sympy.Rational(a,b))
    if sympy.log(s[1],2) % 1 != 0:
        return 'impossible'
    y = sympy.ceiling(sympy.log(s[1]/s[0],2))
    if y > 40:
        return 'impossible'
    else:
        return str(y)

content = [i.rstrip().split('/') for i in open('large.in').readlines()]
for i in range(int(content.pop(0)[0])):
    print('Case #' + str(i+1) + ': ' + solve(int(content[0][0]), int(content.pop(0)[1])))

