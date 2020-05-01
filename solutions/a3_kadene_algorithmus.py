def max_subarray(numbers):
    best_sum = numbers[0] 
    current_sum = numbers[0]
    for x in numbers[1:]:
        
        if current_sum < 0 and x > 0:
            current_sum = x
        else:
            current_sum = max(0 if x >= 0 else x, current_sum + x)
                
        best_sum = max(best_sum, current_sum)
    return best_sum