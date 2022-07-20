# xs = [()] 
# print(xs)
# res = [False] * 2 
# if xs: 
#     res[0] = True 
# if xs[0]: 
#     res[1] = True
    
# print(res)


# x = 17
# y = 13
 
# print(x//y)

index = 0
numbers = [3, 3, 5, 2, 3]
final_result = 0
x = 0
for i, k in  enumerate(numbers):
    # print(i, k)
    if k == 0:
        
        
        # print("im here")
        print("Ended")
    else:
        x = k
        index = i
        break
    
    
print(x)
        
        # x = k
        
        # res = k - x
        # print(k, x)
        
        # if k < x:
        #     print("im here")
            
        #     final_result = final_result + x
        # else:
        #     result = k- x
            
            
            

for t, k in enumerate(numbers):
# for t, k in range(index, len(numbers)-index):
    res = k - x
    print(k, x)
        
    if k < x:
        print("im here")
        
        final_result = final_result + x
    else:
        result = k - x

print(final_result)
       