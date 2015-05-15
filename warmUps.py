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
    if (talking == True) and (hour < 7 or hour > 20):
        return True
    else:
        return False
    
def makes10(a, b):
    if (a + b == 10) or (a == 10 or b == 10):
        return True
    else:
        return False
    
def near_hundred(n):
    if n in range(90,111) or n in range(190, 211):
        return True
    else:
        return False
        
def pos_neg(a, b, negative):
    if (negative == True) and (a < 0 and b < 0):
        return True
    elif (negative == True) and (a > 0 or b > 0):
        return False
    elif (a < 0 and b > 0) or (a > 0 and b < 0):
        return True
    else:
        return False
    
def not_string(str):
    if len(str) >= 3 and ((str[0] == 'n') and (str[1] == 'o') and (str[2] == 't')):
        return str
    else:
        return "not " + str
    
def missing_char(str, n):
    if len(str) >= 0:
        newStr = str.replace(str[n], '')
        return newStr
    
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        length = len(str) - 1
        return str[-1] + str[1:(length)] + str[0]
    
def front3(str):
    if len(str) <= 3:
        return str * 3
    else:
        return (str[0] + str[1] + str[2]) * 3
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    