import logging
import objetos

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
    
    #------------------------------------------ ORDENANMENTO ----------------------------------------------
    
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

#------------------------------------------ DATA -------------------------------------------
def ordenarData(lista,ini,fim,inv,prox):
    
    if(len(lista)==1):
        return lista
    
    a=list()
    # m=list()
    # d=list()
    r=list()
    # k=list()
    p=list()
    c=0
    
    for i in lista:
        a.append(int(i.getData()[ini:fim]))
        # m.append(i.getData()[3:5])
        # d.append(i.getData()[:2])
    
    a=list(set(quick_sort(a)))
    print(a)
    
    # if (inv=='D'):
    #     a=list(reversed(a))
    
    while(c<=len(a)-1):
        
        for i in lista:
            if (int(i.getData()[ini:fim])==a[c]):
                r.append(i)
        # print(r)
        
        if(ini==0 and len(r)>1):
            if(prox['d']=='v'):
                p.extend(ordenarValor(r,inv,prox))
            if(prox['d']=='n'):
                pass
        else:
            p.extend(ordenarData(r,ini-3,fim-3,inv,prox))
        
        x=list()
        for i in p: x.append(i.getData())
        print('P: '+str(x))
        
        r=list()
        c+=1
    
    # for b in a:
    #     for i in r:   
    #         if (b==i):
    #             k.append(i)
                
    #     p.append(ordenarData(k,ini-3,fim-3,inv))
    
    if (inv['dataT']=='D'):
        # print('oi')
        p=list(reversed(p))
    
    x=list()
    for i in p: x.append(i.getData())
    print('P: '+str(x))
    
    return  p


#------------------------------------------------ VALOR -----------------------------------------------------
def ordenarValor(lista,inv,prox):
    
    if(len(lista)==1):
       return lista
      
    a=list()
    p=list()
    r=list()
    c=0
    
    for i in lista:
        a.append(int(i.getValor()))
    
    a=list(set(quick_sort(a)))
    print(a)
    
    while(c<=len(a)-1):
        
        for i in lista:
            if (int(i.getValor())==a[c]):
                r.append(i)
        # print(r)
    
        if(len(r)>1):
            if(prox['v']=='d'):
                p.extend(ordenarData(r,6,8,inv,prox))
            if(prox['v']=='n'):
                pass
        else:
            p.extend(r)
        
        x=list()
        for i in p: x.append(i.getValor())
        print('P: '+str(x))
        
        r=list()
        c+=1
    
    if (inv['valorT']=='D'):
        # print('oi')
        p=list(reversed(p))   
    
    return p

#-------------------------------------------------- NOME ---------------------------------------------------
def ordenarNome(lista,inv,prox):
    pass

#--------------------------------------------------- BUSCA -------------------------------------------------
def ordenaBusca(info,lista):
    
    #DATA
    if (info['data']=='1'):
        if (info['valor']=='2'):
            if(type(lista[0])==objetos.Entrada):
                return ordenarData(lista,6,8,info,{'d':'v','v':'n'})
            else:
                return ordenarData(lista,6,8,info,{'d':'v','v':'i'})
        elif (info['nome']=='2'):
            if(type(lista[0])==objetos.Entrada):
                return ordenarData(lista,6,8,info,{'d':'n','n':'v'})
            else:
                logging.warning('[>] ERRO')
                return []
        else:
            logging.warning('[>] ERRO')
            return []
    
    #VALOR
    elif (info['valor']=='1'):
        ordenarValor()
        if (info['data']=='2'):
            pass
        elif (info['nome']=='2'):
            if(type(inter[0])==objetos.Entrada):
                inter=ordenarNome()
        else:
            logging.warning('[>] ERRO')
            return []
    
    #NOME
    elif (info['nome']=='1'):
        if(type(inter[0])==objetos.Entrada):
                inter=ordenarNome()
        if (info['data']=='2'):
            pass
        elif (info['valor']=='2'):
            pass
        else:
            logging.warning('[>] ERRO')
            return []
    
    #ERRO
    else:
        logging.warning('[>] ERRO')
        return []
    
    

# a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
# print(list(reversed(a)))
# print(quick_sort(a))