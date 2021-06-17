def analiseData(data):
    try:
        if(int(data[:2])>31 or int(data[:2])<=0 or
            int(data[3:5])>12 or int(data[3:5])<=0 or
            int(data[6:8])<=0):
            
            return False
        else:
            
            return True
    except:
        
        return False
    
def ordenarData():
    pass

def ordenarValor():
    pass

def ordenarNome():
    pass