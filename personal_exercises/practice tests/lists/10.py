# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
# [
#     [
#         [[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]
#     ],
    
#     [
#         [[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]
#     ],
    
#     [
#         [[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]
#     ]
# ]
array_3d = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]

print(array_3d)