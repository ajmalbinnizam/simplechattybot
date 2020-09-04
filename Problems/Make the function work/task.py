# def closest_higher_mod_5(x):
#     y = x % 5
#     if y==0:
#         return x
#     z=5-y
#     return x+z
#
# x=int(input())
# print(closest_higher_mod_5(x))
def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    y = x
    y = 5 - (x % 5)
    return x + y
closest_higher_mod_5(40)