import os
import glob
import pickle
from objetos import Entrada, User, Saida
import logging


def buscaSaidas(user,filtros):
    
    resultado=list()
    lis=list()
    
    diretorio=os.listdir('db/logs/user'+str(user.getId()+1)+'/registry/saida/')
    diretorio.remove('types.pck')
    
    #REGISTROS VAZIOS
    if(diretorio==[]):
        return resultado
    
    
    #DATA
    if(filtros['inicioDATA']!=''):
        
        n=int(filtros['inicioDATA'][6:8])-int(filtros['fimDATA'][6:8])+1 
        c=0
        
        #ANO
        while(c<n):
            if('20'+str(int(filtros['inicioDATA'][6:8])+c) in diretorio):
                # lis.append('20'+str(int(filtros['inicioDATA'][6:8])+c))                
                
                #MES
                meses=os.listdir('db/logs/user'+str(user.getId()+1)+'/registry/saida/20'+str(int(filtros['inicioDATA'][6:8])+c))
                
                #INICIO
                if(str(int(filtros['inicioDATA'][6:8])+c)==filtros['inicioDATA'][6:8]):                    
                    for i in meses:
                        if(int(i)>=int(filtros['inicioDATA'][3:5])):
                            arq=open('db/logs/user'+str(user.getId()+1)+'/registry/saida/20'+str(int(filtros['inicioDATA'][6:8])+c)+'/'+i+'/info.pck',"rb")
                            dias=pickle.load(arq)
                            arq.close()
                            for d in dias:
                                if(int(d.getData()[:2])>=int(filtros['inicioDATA'][:2])):
                                    lis.append(d)
                
                #FIM
                elif(str(int(filtros['inicioDATA'][6:8])+c)==filtros['fimDATA'][6:8]):
                    for i in meses:
                        if(int(i)<=int(filtros['fimDATA'][3:5])):
                            arq=open('db/logs/user'+str(user.getId()+1)+'/registry/saida/20'+str(int(filtros['inicioDATA'][6:8])+c)+'/'+i+'/info.pck',"rb")
                            dias=pickle.load(arq)
                            arq.close()
                            for d in dias:
                                if(int(d.getData()[:2])<=int(filtros['inicioDATA'][:2])):
                                    lis.append(d)
                        else:
                            break
                #MEIO
                else:
                    for i in meses:
                        arq=open('db/logs/user'+str(user.getId()+1)+'/registry/saida/20'+str(int(filtros['inicioDATA'][6:8])+c)+'/'+i+'/info.pck',"rb")
                        dias=pickle.load(arq)
                        arq.close()
                        lis.extend(dias)   
            
            c+=1
        
        if(lis==[]):
            return resultado
        
        
        if(filtros['tipos']!=[]):
            for i in lis:
                if(i.getTipo() in filtros['tipos']):
                    resultado.append(i)
            lis=[]
            if(filtros['VAL1']!=''):
                for i in resultado:
                    if(i.getValor()>=filtros['VAL1'] and i.getValor()<=filtros['VAL2']):
                        lis.append(i)
                resultado=lis
        
        elif(filtros['VAL1']!=''):
            for i in lis:
                if(i.getValor()>=filtros['VAL1'] and i.getValor()<=filtros['VAL2']):
                    resultado.append(i)
        
    
    #TIPOS
    elif(filtros['tipos']!=[]):
        for i in diretorio:
            meses=os.listdir('db/logs/user'+str(user.getId()+1)+'/registry/saida/'+i+'/')
            for k in meses:
                arq=open('db/logs/user'+str(user.getId()+1)+'/registry/saida/'+i+'/'+k+'/info.pck',"rb")
                dias=pickle.load(arq)
                arq.close()
                lis.extend(dias)
        print(lis)
        for i in lis:
            if(i.getTipo==filtros['tipos']):
                    resultado.append(i)
        
        lis=[]
        if(filtros['VAL1']!=''):
            for i in resultado:
                if(i.getValor()>=filtros['VAL1'] and i.getValor()<=filtros['VAL2']):
                    lis.append(i)
            resultado=lis
    
    #VALOR
    elif(filtros['VAL1']!=''):
        for i in diretorio:
            meses=os.listdir('db/logs/user'+str(user.getId()+1)+'/registry/saida/'+i+'/')
            for k in meses:
                arq=open('db/logs/user'+str(user.getId()+1)+'/registry/saida/'+i+'/'+k+'/info.pck',"rb")
                dias=pickle.load(arq)
                arq.close()
                lis.extend(dias)
        
        for i in lis:
                if(i.getValor()>=filtros['VAL1'] and i.getValor()<=filtros['VAL2']):
                    resultado.append(i)
    
    #TUDO
    else:
        for i in diretorio:
            meses=os.listdir('db/logs/user'+str(user.getId()+1)+'/registry/saida/'+i+'/')
            for k in meses:
                arq=open('db/logs/user'+str(user.getId()+1)+'/registry/saida/'+i+'/'+k+'/info.pck',"rb")
                dias=pickle.load(arq)
                arq.close()
                resultado.extend(dias)    
    
    return resultado


#---------------------------------------------------------REGISTROS-----------------------------------------------------------

def registryENTRADA(entrada,id):
    lista=list()
    data=entrada.getData()
    try:
        arq=open('db/logs/user'+str(id+1)+'/registry/entrada/20'+data[6:8]+'/'+data[3:5]+'/info.pck','rb')
    except:
        try:
            os.mkdir('db/logs/user'+str(id+1)+'/registry/entrada/20'+data[6:8])
        except:
            logging.warning("Ano já Existente")
        os.mkdir('db/logs/user'+str(id+1)+'/registry/entrada/20'+data[6:8]+'/'+data[3:5])
        arq=open('db/logs/user'+str(id+1)+'/registry/entrada/20'+data[6:8]+'/'+data[3:5]+'/info.pck','wb')
        lista.append(entrada)
        pickle.dump(lista,arq)
    else:
        lista.extend(pickle.load(arq))
        lista.append(entrada)
        arq.close()
        arq=open('db/logs/user'+str(id+1)+'/registry/entrada/20'+data[6:8]+'/'+data[3:5]+'/info.pck','wb')
        pickle.dump(lista,arq)
        
    arq.close()

def registrySAIDA(saida,id):
    lista=list()
    data=saida.getData()
    try:
        arq=open('db/logs/user'+str(id+1)+'/registry/saida/20'+data[6:8]+'/'+data[3:5]+'/info.pck','rb')
    except:
        try:
            os.mkdir('db/logs/user'+str(id+1)+'/registry/saida/20'+data[6:8])
        except:
            logging.warning("Ano já Existente")
        os.mkdir('db/logs/user'+str(id+1)+'/registry/saida/20'+data[6:8]+'/'+data[3:5])
        arq=open('db/logs/user'+str(id+1)+'/registry/saida/20'+data[6:8]+'/'+data[3:5]+'/info.pck','wb')
        lista.append(saida)
        pickle.dump(lista,arq)
    else:
        lista.extend(pickle.load(arq))
        lista.append(saida)
        arq.close()
        arq=open('db/logs/user'+str(id+1)+'/registry/saida/20'+data[6:8]+'/'+data[3:5]+'/info.pck','wb')
        pickle.dump(lista,arq)
        
    arq.close()
    
def consultaTipos(user,meio,new):
    arq=open('db/logs/user'+str(user.getId()+1)+'/registry/'+meio+'/types.pck',"rb")
    lista=pickle.load(arq)
    for i in lista:
            if i==new:
                return True   
    arq.close()
    return False

def criaTipo(user,meio,new):
    arq=open('db/logs/user'+str(user.getId()+1)+'/registry/'+meio+'/types.pck',"rb")
    lista=pickle.load(arq)
    arq.close()
    lista.append(new)
    arq=open('db/logs/user'+str(user.getId()+1)+'/registry/'+meio+'/types.pck',"wb")
    pickle.dump(lista,arq)
    arq.close()

def consultaInfo(acrs):
    arq=open('db/'+acrs+'info.pck','rb')
    n=int(pickle.load(arq))
    arq.close()
    return n

def atualizaInfo(n):
    v=int(int(consultaInfo(''))+int(n))
    arq=open('db/info.pck','wb')
    pickle.dump(v,arq)#int(int(consultaInfo())+int(n))
    arq.close()
    

def criarUser(usuario,senha):
    lista=list()
    arq=open('db/users.pck',"rb")   
    
    try:
        ret=pickle.load(arq)
        arq.close()
        
    except:
        obj=User(usuario,senha) 
        lista=[obj]                   
    else:   
        lista.extend(ret)
        for i in lista:
            if i.getUser()==usuario:
                return False   
        obj=User(usuario,senha)
        lista.append(obj)
        
    arq=open('db/users.pck',"wb")
    pickle.dump(lista, arq)
    arq.close()
    atualizaInfo(1)
    
    #PASTAS PADRÃO
    os.mkdir("db/logs/user"+str(consultaInfo('')))
    os.mkdir("db/logs/user"+str(consultaInfo(''))+"/registry")
    os.mkdir("db/logs/user"+str(consultaInfo(''))+"/registry/entrada")
    os.mkdir("db/logs/user"+str(consultaInfo(''))+"/registry/saida")
    
    #PASTAS PADRÃO
    
    #NUMERO DE REGISTROS
    arq=open("db/logs/user"+str(consultaInfo(''))+"/registry/info.pck",'wb')
    pickle.dump(0,arq)
    arq.close()
    
    #TIPOS DE ENTRADAS
    arq=open("db/logs/user"+str(consultaInfo(''))+"/registry/entrada/types.pck",'wb')
    pickle.dump(['DÍZIMO MENSAL', 'DÍZIMO SEMANAL', 'OFERTA', 'OFERTA ESPECIAL', 'CRIAR++'],arq)
    arq.close()
    
    #TIPOS DE SAÍDA
    arq=open("db/logs/user"+str(consultaInfo(''))+"/registry/saida/types.pck",'wb')
    pickle.dump(['ÁGUA','LUZ','CONTABILIDADE','ALUGUEL','PASTOR','FAP','13º PASTOR','FÉRIAS PASTOR',
    'ZELADOR','13º ZELADOR','PRESBITERIO','SUPREMO CONCILIO','INSS','IRRF','PLANO SAÚDE','EMPRESTIMOS',
    'BENEFICIÊNCIA','CONSTRUÇÃO / REFORMA','INSTRUMENTOS','USO CONSUMO','FESTIVIDADE','ESCOLA DOMINICAL',
    'CORAL','UCP','UPA','UMP','SAF','UPH','VAN','BANCO','IPTU','CARTORIO','TRANSPORTE', 'CRIAR++'],arq)
    arq.close()
    
    return True

def deletUser(usuario,senha):
    lista=list()
    c=0
    arq=open('db/users.pck',"rb")
    lista.extend(pickle.load(arq))
    arq.close()
    if consultUser(usuario)==False:
        return False    
    for i in lista:
            if i.getUser()==usuario:
                if i.getSenha()==senha:
                    arq=open('db/users.pck',"wb")
                    del(lista[c])
                    pickle.dump(lista,arq)
                    arq.close()
                    return True
            c+=1
    
    return False 


def consultUser(usuario):
    if consultaInfo('')==0:
        return False
    arq=open('db/users.pck',"rb")
    lista=pickle.load(arq)
    for i in lista:
            if i.getUser()==usuario:
                return True   
    arq.close()
    return False


def consultSenha(usuario,senha):
    arq=open('db/users.pck',"rb")
    lista=pickle.load(arq)
    for i in lista:
            if i.getUser()==usuario:
                if i.getSenha()==senha:
                    return True   
    arq.close()
    return False

def listatUsers():
    lista=list()
    arq=open('db/users.pck',"rb")
    lista.extend(pickle.load(arq))
    arq.close()
    return lista

def consultaQtd():
    return len(listatUsers())

def getIsntanc(usuario):
    arq=open('db/users.pck',"rb")
    lista=pickle.load(arq)
    for i in lista:
            if i.getUser()==usuario:            
                return i   

def getTypesENTRADA(id):
    Id=id+1
    arq=open("db/logs/user"+str(Id)+"/registry/entrada/types.pck",'rb')
    lista=pickle.load(arq)
    arq.close()
    return lista

def getTypesSAIDA(id):
    Id=id+1
    arq=open("db/logs/user"+str(Id)+"/registry/saida/types.pck",'rb')
    lista=pickle.load(arq)
    arq.close()
    return lista



# arq=open('db/users.pck',"wb")
# # l1=[1,2,3]
# # pickle.dump(l1, arq)
# arq.close()

# print(criarUser('arthur','123'))
# print(criarUser('Pericles','adm123'))
# arq=open('db/users.pck',"rb")
# r=pickle.load(arq)
# arq.close()
# print(r)

# arq=open('db/logs/user1/registry/entrada/2021/03/info.pck','rb')
# print(type(pickle.load(arq)))
# arq.close()


# arq=open('db/info.pck','rb')
# print(pickle.load(arq))
# arq.close()


# arq=open('db/info.pck','wb')
# pickle.dump(0,arq)
# arq.close()
