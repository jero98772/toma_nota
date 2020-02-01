dia = int(input("dia nacimiento \t"))
mes = int(input("mes el cual nacio \t"))
años = int(input("año de nacimiento  \t"))
añosendias=int(input("cuantos dias cree que a vivido o para calular cuantso años tienen esos dias \t"))   
#entradas del usiario
class eddad:
    def variables(self,dias,mes,años):
        #sistema de medicion
        self.D = 30
        self.M = 12
        self.A = 2020 
        self.años = años
        self.mes = mes
        self.dias = dias
                
    def eddadendias(self):

        print ("fecha es usted nacio el ?",self.dias,"dia \t ",self.mes,"mes \t",self.años,"año")
        #dias de 2020 años o self.A
        self.añosdias = (self.A*self.M*self.D)
        #self.años en dias
        self.AÑOSdias = (self.años*self.M*self.D)
        #self.meses en dias
        self.MESESdias = (self.mes*self.D)
        
        self.eddad_dias = self.añosdias-self.AÑOSdias-self.MESESdias-self.dias
        #print ("eddad en dias",self.eddad_dias,)
        return self.eddad_dias
    def eddadenaños(self ,eddad_dias=None):
        
        if  eddad_dias == None:
            self.eddad_dias 
        else :
            self.eddad_dias = eddad_dias
            print("seguro que tiene ?",self.eddad_dias ,"dias")
        self.eddad = self.eddad_dias / (self.D * self.M)
        return self.eddad
        #print("usted tiene ", self.eddad ,"años")
eddad=eddad()
eddad.variables(dia,mes,años)

eddad_dias=eddad.eddadendias()
print ("eddad en dias",eddad_dias,)

eddad_con_dias= eddad.eddadenaños()
print("usted tiene ", eddad_con_dias,"años")

eddadposblible =eddad.eddadenaños(añosendias)
print("usted tiene ", eddadposblible ,"años")
