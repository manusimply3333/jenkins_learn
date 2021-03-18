# ==== Decorator =========
# def upr_msg(fun1):
#     def inner():
#         a = fun1()
#         #print(a())
#         return a.upper()
#     return inner
# @upr_msg
# def msg():
#     return "this is msg"
# #b = upr_msg(msg)
# print(str(msg()))

#==Decorator with Arguments ===


def div_decor(fun):
    def inner(a,b):
        if a < b:
            a,b = b,a
            return a,b
    return inner(a,b)
@div_decor
def div(a,b):
    return a/b

print(div(2,3))