import logging

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
    
def ordenarData(lista):
    a=list()
    m=list()
    d=list()
    
    for i in lista:
        a.append(i.getData()[6:8])
        m.append(i.getData()[3:5])
        d.append(i.getData()[:2])
    PERDA DE REFERÊNCIA INICIAL APÓS A ORDENAÇÃO

def ordenarValor():
    pass

def ordenarNome():
    pass

def ordenaBusca(info,lista):
    if (info['data']=='1'):
        ordenarData()
        if (info['valor']=='2'):
            pass
        elif (info['nome']=='2'):
            pass
        else:
            logging.warning('[>] ERRO')
    elif (info['valor']=='1'):
        ordenarValor()
        if (info['data']=='2'):
            pass
        elif (info['nome']=='2'):
            pass
        else:
            logging.warning('[>] ERRO')
    elif (info['nome']=='1'):
        ordenarNome()
        if (info['data']=='2'):
            pass
        elif (info['valor']=='2'):
            pass
        else:
            logging.warning('[>] ERRO')
    else:
        logging.warning('[>] ERRO')
    
    



def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):

    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1

a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
print(list(reversed(a)))
print(quick_sort(a))