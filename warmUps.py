def sleep_in(weekday, vacation):
    if (weekday == False or vacation == True):
        return True
    else:
        return False
    
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
    
def sum_double(a, b):
    if (a == b):
        return (a+b) * 2
    else:
        return a + b
    
def diff21(n):
    difference = n - 21
    if difference < 0:
        difference = difference * -1
        if n > 21:
            return difference * 2
        else:
            return difference
    else:
        if n > 21:
            return difference * 2
        else:
            return difference
        
def parrot_trouble(talking, hour):
    if (talking == False) and (hour in range(7,20)):
        return False
    else:
        return True