from operator import index


vector1 = [1,2,3]
vector2 = [-1,0,2]
result_sum = 0

for index in range (len(vector1)):
    result_sum += (vector1[index] * vector2[index])
    
print ("Tu producto escalar es", result_sum)
