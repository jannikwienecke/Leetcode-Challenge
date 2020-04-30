def single_number(l):
    set_numbers = set()
    
    for number in l:
        if number in set_numbers:
            set_numbers.remove()
    else:
        set_numbers.add(number)
        
    return next(iter(set_numbers))