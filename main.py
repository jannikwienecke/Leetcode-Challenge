import solutions

# CHALLENGE #1 ---------------------------------------
input_list = [1,4,4,1,2]
result_1 = solutions.a1.single_number(input_list)
print(f"Single Number: Input: {input_list} - Result: {result_1}")

# CHALLENGE #2 ---------------------------------------
input_number = 22
result_2 = solutions.a2.happy_number(input_number)
print(f"Happy Number: Input: {input_number} - Result: {result_2}")

# CHALLENGE #3 ---------------------------------------
input_list=  [-2,1,-3,4,-1,2,1,-5,4]
result_3 = solutions.a3_kadene_algorithmus.max_subarray(input_list)
print(f"max_subarray: Input: {input_list} - Result: {result_3}")

# CHALLENGE #4 ---------------------------------------
input_list = [0,1,0,3,12]
result = solutions.a4.move_zeros(input_list)
print(f"move_zeros: Input: {input_list} - Result: {result}")

# CHALLENGE #5 ---------------------------------------
lst = [7,1,5,3,6,4]
result = solutions.a5.stock_standard(lst)
print(f"Stock Market: Input: {lst} - Result: {result}")

result = solutions.a5.stock_advanced(lst)
print(f"Stock Market - Advanced: Input: {lst} - Result: {result}")



