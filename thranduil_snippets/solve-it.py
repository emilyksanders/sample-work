#! /usr/bin/env python3

# Raw input
a = [ 2,  5,  2, -38]
b = [ 3, -2,  4,  17]
c = [-6,  1, -7, -12]
print("Raw input:")
print("a:", a)
print("b:", b)
print("c:", c)
print("")

# Normalized input
coef_abc = abs(a[0]*b[0]*c[0])
a = [coef_abc*i/a[0] for i in a]
b = [coef_abc*i/b[0] for i in b]
c = [coef_abc*i/c[0] for i in c]
print("Normalized input:")
print("a:", a)
print("b:", b)
print("c:", c)
print("")

# calculate differences
a_minus_b = [i - j for i, j in list(zip(a, b))][1:]
a_minus_c = [i - j for i, j in list(zip(a, c))][1:]
print("Differences:")
print("a_minus_b:", a_minus_b)
print("a_minus_c:", a_minus_c)
print("")

# normalize differences
coef_bc = abs(a_minus_b[0]*a_minus_c[0])
a_minus_b = [coef_bc*i/a_minus_b[0] for i in a_minus_b]
a_minus_c = [coef_bc*i/a_minus_c[0] for i in a_minus_c]
print("Normalized Differences:")
print("a_minus_b:", a_minus_b)
print("a_minus_c:", a_minus_c)
print("")

# calculate differences
b_minus_c = [i - j for i, j in list(zip(a_minus_c, a_minus_b))][1:]
print("Differences:")
print("b_minus_c:", b_minus_c)
print("")

# plugin in values
z = b_minus_c[1]/b_minus_c[0]
y = (a_minus_b[2] - a_minus_b[1]*z)/coef_bc
x = (a[3] - a[2]*z - a[1]*y)/coef_abc
print("Results:")
print([x, y ,z])
print("")
