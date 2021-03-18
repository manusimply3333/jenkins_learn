import re
#st = "Manoj is 22 and Rajesh is 23 email manoj_kumar99@gmail.com"
#ip = "system ip is 120.212.32.321"

#^[a-z]{1,6}_?\d{0,4}@+hackerrank.com

# ages =  re.findall(r'\d{1,4}',st)
# print(ages)

#finip = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',ip)
#print(finip)


# findname = re.findall(r'[A-Z][a-z]*',st)
# print(findname)
#^[a-z]{1,6}_?\d{0,4}@+hackerrank.com

#find_email = re.findall(r'[^a-z]*[_]{1}\d{1,2}@[a-z].[a-z]',st)
#find_email = re.findall('\S+@\S+', st)
# find_email = re.findall(r"\w*_?\d{1,2}@+gmail.com",st)
# print(find_email)
# def funct(l):
#     l.append(6)
#     return l
# l = [1,2,3,4,5]
# print(funct(l))
# print(funct(l=[]))
# print(funct(l))

# n = 0
# n1 = 1
# count  = 0
# last = int(input("number please"))
# while count < last:
#     print(n)
#     nth = n+n1
#     n = n1
#     n1 = nth
#     count = count+1
#sorting program
# list1 = [1,22,13,43,21,45,223,45]
# list2 = []
# while list1:
#     m = list1[0]
#     for i in list1:
#         if i < m:
#             m = i
#     list2.append(m)
#     list1.remove(m)
# print(list2)

#remove special characters
#string = "abc@#$%^1234jihcsc%^&*"
# new_string = ""
# for c in string:
#     if c.isalpha():
#         new_string =c+new_string
# print(new_string)

# ans  = re.findall(r'[a-z]',string)
# fin = "".join(ans)
# print(fin)

l1 = "manoj kumar prajapati"
l2 = l1.split(" ")
st = ""
print(l2)
#last = len(l2)
last_con = l2[-1]
print(last_con)
for c in last_con:
    st = c+st
print(st)


