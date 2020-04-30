def happy_number(number):
    track_numbers = set()
    for x in range(40):
        sum_ = 0
        for num in str(number):
            sum_ += int(num) ** 2
        
        if sum_ == 1:
            return True
        
        if number in track_numbers:
            return False
        
        track_numbers.add(number)
        number = sum_