# this solutions also delivers the array which is the max
# subarray. Therefore it keeps track of the start and the
# end of the subarray

def maximum_subarray(arr):
    
    start_max = 0
    end_max = 0
    start_current = 0
    end_current = 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    for index, num in enumerate(arr):
        if index ==0 :
            continue 
            
        if max_sum <= 0 and num > max_sum:  
            current_sum = num
            max_sum = num

            start_max = index
            end_max = index
            start_current = index
            end_current = index
            
            
        elif current_sum + num <= max_sum:            
            if current_sum >= 0 and current_sum + num < 0:
                current_sum = 0
                start_current = index+1
                end_current = index+1
                
            else:
                current_sum += num
                end_current = index
                
        else:
            current_sum += num
            max_sum = current_sum
            end_current = index
            start_max = start_current
            end_max = end_current
            
        
    print("MAX IST = ", max_sum)
    print('arr = ', arr[start_max: end_max+1])
    
    return max_sum