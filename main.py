l = [2,2,1]
l1 = [1,2,2,3,4,5,4,5,1,6,9,9]

def single_number(l):
    set_numbers = set()
    
    for number in l:
        if number in set_numbers:
            set_numbers.remove()
    else:
        set_numbers.add(number)
        
    return next(iter(set_numbers))

print(single_number(l1))