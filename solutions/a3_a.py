# this solutions is only calculating the max value of the
# subarray but does not give the corresponding array

def maximum_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for index, num in enumerate(arr):
        if index ==0 :
            continue 
            
        if max_sum <= 0 and num > max_sum:  
            current_sum = num
            max_sum = num
            
        elif current_sum + num <= max_sum:            
            if current_sum >= 0 and current_sum + num < 0:
                current_sum = 0
                
            else:
                current_sum += num
                
        else:
            current_sum += num
            max_sum = current_sum
            
    return max_sum