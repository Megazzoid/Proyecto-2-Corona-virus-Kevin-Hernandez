class Candidato: #Se crea clase principal 
    def __init__(self,nombre,edad):

        self.nombre = nombre
        self.edad = edad     
        

    def informacion(self): #funcion para imprimir datos
        return 'Nombre completo: {}\nEdad: {}\n'.format(self.nombre, self.edad)


class Posible_infectado(Candidato): #Se hace herencia 
     def __init__(self,nombre,edad,cuidad,direccion,estado):
        Candidato.__init__(self,nombre,edad)
        self.cuidad = cuidad
        self.direccion = direccion
        self.estado = estado
     def informacion2(self): #funcion para imprimir datos
        return 'Nombre completo: {}\nEdad: {}\nCuidad: {}\nDireccion: {}\nEstado: {}\n'.format(self.nombre, self.edad, self.cuidad, self.direccion, self.estado)
        


class No_infectado(Candidato): #Se hace herencia 
     def __init__(self,nombre,edad,telefono):
        Candidato.__init__(self,nombre,edad)
        self.telefono = telefono
     def informacion(self): #Funcion para imprimir datos
        return 'Nombre completo: {}\nEdad: {}\nTelefono {}\n'.format(self.nombre, self.edad, self.telefono)
          

       
class Infectado(Candidato): #Se hace herencia
    def __init__(self,nombre,edad,cuidad,direccion,estado,medico):
        Candidato.__init__(self,nombre,edad)
        self.cuidad = cuidad
        self.direccion = direccion
        self.estado = estado 
        self.medico = medico
    def informacion3(self): #Funcion para imprimir datos
        return 'Nombre completo: {}\nEdad: {}\nCuidad: {}\nDireccion: {}\nEstado: {}\nMedico Tratante: {}\n'.format(self.nombre, self.edad, self.cuidad, self.direccion, self.estado,self.medico)    
    
    
        
        
