import arq_control

class User:
    def __init__(self,user,senha):
        self.id=arq_control.consultaInfo('')
        self.user=user
        self.senha=senha
        
    def getId(self):
        return self.id
    
    def getUser(self):
        return self.user
    
    def getSenha(self):    
        return self.senha
    
    
class Entrada:
    def __init__(self,valor,tipo,nome,data,user):
        self.id=arq_control.consultaInfo("logs/user"+str((user.getId()+1))+"/registry/")
        self.valor=valor
        self.tipo=tipo
        self.nome=nome
        self.data=data
        arq_control.registryENTRADA(self,user.getId())

    def getId(self):
        return self.id
    
    def getValor(self):
        return self.valor
    
    def getTipo(self):
        return self.tipo
    
    def getNome(self):
        return self.nome
    
    def getData(self):
        return self.data

    
class Saida:
    def __init__(self,valor,tipo,data,user):
        self.id=arq_control.consultaInfo("logs/user"+str((user.getId()+1))+"/registry/")
        self.valor=valor
        self.tipo=tipo
        self.data=data
        arq_control.registrySAIDA(self,user.getId())
        
    def getId(self):
        return self.id
    
    def getValor(self):
        return self.valor
    
    def getTipo(self):
        return self.tipo
    
    def getData(self):
        return self.data