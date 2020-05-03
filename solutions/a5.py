def stock_standard(lst):
    total_win = 0
    for i, price in enumerate(lst[1:]):
        total_win += price - lst[i] if price > lst[i] else 0
    return total_win


def stock_advanced(lst):
    
    def sell_stock(i):
        nonlocal total_win
        for price_bought in bought_at:
            total_win += lst[i] - price_bought  
            
    total_win = 0
    bought_at = set()
    
    for i, price in enumerate(lst[1:]):
        if price > lst[i]:
            bought_at.add(lst[i])
        elif bought_at:
            sell_stock(i)
            bought_at = set()
            
        # on last day sell all stocks
        if i + 2 == len(lst):
            sell_stock(i+1)
    
    return total_win


