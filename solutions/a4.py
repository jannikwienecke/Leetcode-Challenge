def move_zeros(lst):
    nxt = 0
    for x in lst:
        if x:
            lst[nxt] = x
            nxt += 1
            
    for index in range(nxt, len(lst)):
        lst[index] = 0
