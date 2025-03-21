def checkIfNotNumeric(*var):
    for i in var:
        if not(isinstance(i,(int,float))):
            return False
    return True

def AddAllNumerics(*args):
    total = 0
    for x in args:
        total += x
    return total
        
            

