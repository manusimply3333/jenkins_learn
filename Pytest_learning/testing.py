# num = 16
# for i in range(2,num):
#     if num % 2 == 0:
#         print("Number is not prime")
#         break
# else:
#     print("number is prime")

fd = open("file1.text","rt")
temp_list = []
for line in fd.readlines():
    temp = line.replace("pyar","=====")
    temp_list.append(temp)
fd.close()
print(temp_list)
fd = open("file1.text", "w")
for l in temp_list:
    fd.write(l)

# for line in fd:
#     if "hate" in line:
#         dum = line.replace("hate","love")
#         temp_list.append(dum)
#
# fd = open("file1.text","w")
#     for line in temp_list:
#         fd.write(line)
