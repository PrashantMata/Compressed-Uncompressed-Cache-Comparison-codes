import random
#import matplotlib.pyplot as plt
#import numpy as np
#N=10
#x = np.arange(N)
lst = []
hexFinal_lst = []
uncompressed_lst = [] 
compressed_lst = []
foo =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 68, 72, 464, 465, 466, 467, 472, 473, 474, 475, 504, 505, 506, 507, 508, 509,510, 511]


for i in range(600):
    ele = random.choice(foo)
    lst.append(ele)
print (lst)

Mul_lst = [i * 4 for i in lst]
hex_lst = [hex(i) for i in Mul_lst]
hex1_lst = [i.replace("0x","") for i in hex_lst]
hexZero_lst = [i.zfill(3) for i in hex1_lst]
#hexFinal_lst = ["32'h"+" "+i+"2a183"+ ";" for i in hexZero_lst]

for i in range(600):
    if (lst[i] <=32):
        kele = ("32'h"+" "+ hexZero_lst[i] +"02183"+ ";")
    else :
        kele = ("32'h"+" "+ hexZero_lst[i] +"2a183"+ ";")
    hexFinal_lst.append(kele)
#print (hexFinal_lst)


print (Mul_lst)
print (hex_lst)
print (hex1_lst)
print (hexZero_lst)
print (hexFinal_lst)

# for j in range(10):
#     if (lst[j]<=32):
#         uncompressed_lst.append(8)
#         compressed_lst.append(8)
#     else :
#         uncompressed_lst.append(50)
#         compressed_lst.append(8)
# print (uncompressed_lst)
# 
# plt.xticks(x, lst)
# plt.bar(x, uncompressed_lst, color ='maroon', width = 0.2)
# plt.bar(x+0.2, compressed_lst, color ='green', width = 0.2)
# plt.legend(['uncompressed_cache', 'compressed_cache'], loc='upper left')
# plt.show()
   
for k in range(600):    
    f1 = open("C:/Users/Prashant Mata/Desktop/address.txt", "a")
    address= 41+k
    if (lst[k] <=32):
        f1.write("\t\tmemory[%d] = %s //    lw x3, %d(x0)  ...   x3 <--memory[%d]\n" %(address, hexFinal_lst[k], Mul_lst[k], lst[k]))
        f1.close()
    else :
        f1.write("\t\tmemory[%d] = %s //    lw x3, %d(x0)  ...   x3 <--memory[%d]\n" %(address, hexFinal_lst[k], Mul_lst[k], lst[k]+256))
        f1.close()
   
    


