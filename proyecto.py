import tkinter as tk
from tkinter import ttk
import math
from tkinter import *


#variables que se usaran

tamañoX=4
tamañoY=4
xI=1
yI=4
xF=4
yF=4
xA=1
yA=int
yA=1
original=True
nBloqueosX=[]
nBloqueosY=[]

class Nodo: #creo el objeto nodo
    def __init__(self,padre,costo,x,y):
        self.padre=padre
        self.costo=costo
        self.x=x
        self.y=y
        self.bloqueado=False
        self.inicio=False
        self.final=False

def nuevo():
    global original
    original=False

def encontrarCamino():# empieza a buscar el camino mas rapido
    global xI
    global yI
    global tamañoX
    global tamañoY
    global xF
    global yF
    global xA
    global yA
    global original
    global nBloqueosX
    global nBloqueosY

    print("Nodo Final:",xF,yF) 
    print("Nodo Inicial:",xI,yI)#verifico que el final este correcto

    nodos=[]

    xA=xI
    yA=yI

    x=1
    if original:
        while x<=tamañoX: #lleno el arreglo con todos los nodos
            y=1
            while y<=tamañoY:
                #print(x,y)
                nuevo=Nodo(None,None,None,None)
                nuevo.x=x
                nuevo.y=y
                if(x==3 and (y==2 or y==3 or y==4)):
                    nuevo.bloqueado=True
                if(x==int(xF) and y==int(yF)):
                    
                    nuevo.final=True
                    #print("---------")
                # print("Encontro Final")
                if(x==xI and y==yI ):
                    nuevo.bloqueado=True
                #   print("encontro inicio")
                    nuevo.inicio=True
                    nuevo.costo=0

                nodos.append(nuevo)

                y+=1
            x+=1
    else:
        print("camino nuevo")
        while x<=tamañoX: #lleno el arreglo con todos los nodos
            y=1
            while y<=tamañoY:
                #print(x,y)
                nuevo=Nodo(None,None,None,None)
                nuevo.x=x
                nuevo.y=y
                if(len(nBloqueosX)>0):
                    bloquear=0
                    while bloquear<len(nBloqueosX):
                        if(nBloqueosX[bloquear]==x and nBloqueosY[bloquear]==y):
                            nuevo.bloqueado=True  
                        bloquear=bloquear+1
                if(x==int(xF) and y==int(yF)):
                    nuevo.final=True
                    #print("---------")
                # print("Encontro Final")
                if(x==xI and y==yI ):
                    nuevo.bloqueado=True
                #   print("encontro inicio")
                    nuevo.inicio=True
                    nuevo.costo=0

                nodos.append(nuevo)

                y+=1
            x+=1
        

    #print(nodos[0].inicio)

    encontro=False
    #rep=0
    #m=0
    movimiento=0
    
    caminoX=[]
    caminoY=[]
   # camino=[[caminoX][caminoY]]

    caminoX.append(xA)
    caminoY.append(yA)

    print(caminoX)
    print(caminoY)
    print("-*-----------------------------------")

    while encontro==False:
        g1=0
        x=1
        nodoNuevo=Nodo(None,None,None,None)
        min=40
        perdido=False
        costos1=[]
        costos2=[]
        suma=0 #suma del total de nodos
        suma2=0 #suma del total de nodos bloqueados o con mayor costo
        while x<=tamañoX:
            y=1
            while y<=tamañoY:
                #print(x,y)
                
                if(y==(yA-1)  or y==yA or y==((yA)+1) ):
                    if(x==((xA)-1) or x==(xA) or x==((xA)+1)):
                        if(x!=xA or y!=yA):
                            
                            for nodo in nodos:
                                #print(nodo.final)
                                if(nodo.x==x and nodo.y==y):

                                    if(nodo.final==True):
                                        encontro=True
                                        caminoX.append(x)
                                        caminoY.append(y)
                                        print("nodo encontrado" , xF, yF)
                                        break
                                    if(nodo.bloqueado==False):
                                        #print(" ")
                                        suma+=1
                                        h = math.sqrt(((int(xF)-int(x))*(int(xF)-int(x)))+((int(yF)-int(y))*(int(yF)-int(y))))
                                        #print(h)
                                        if(x!=xA and y!=yA):
                                            g=1.4
                                            
                                        else:
                                            g=1
                                            
                                        
                                        costos=g+h+movimiento
                                        
                                        costos2.append(costos)
                                        if(nodo.costo==None or costos<=nodo.costo):
                                            nodo.costo=costos
                                            if(costos<min):
                                                min=costos
                                                nodoNuevo.x=x
                                                nodoNuevo.y=y
                                                g1=g

                                            
                                        costos1.append(nodo.costo)

                                        #print("el minimo es",min)
                                        #print(costos)
                                        #print("encontro Vecinos" , x , y ,"y su costo es" , costos) 
                                    #print("no lo encuentra")
                                    else:
                                        suma+=1
                                        suma2+=1
                                       # print(nodo.x,nodo.y)
                            
                y+=1
                if(encontro):
                    break
            x+=1
            if(encontro):
                break
        if(encontro):
            break
        movimiento=movimiento+g1
        posicion=0
        for i in costos1:
            #print(costos2[posicion] , costos1[posicion])
            #print(posicion)
            if(costos2[posicion] > costos1[posicion]):
                #print("encuentra mayor costo en " , costos2[posicion])
                suma2+=1
            posicion=posicion+1
        #print("las relaciones van asi: ", suma,len(costos1),suma2)
        print(costos1)
        print(costos2)
        if(suma==suma2):
            perdido=True
        if(perdido):
            print("Camino cerrado, buscando otro camino")
            for nodo in nodos:
                if(nodo.x==xA and nodo.y==yA):
                     print("-----------------------Reinicando camino--------------------------------")

                     nodo.bloqueado=True
                     print(nodo.x, nodo.y)
            xA=xI
            yA=yI
            movimiento=0
            caminoX=[]
            caminoY=[]
            caminoX.append(xI)
            caminoY.append(yI)
        else:
            if(nodoNuevo.x==None):
                print("no existen caminos posibles")
                break
            else:
                caminoX.append(nodoNuevo.x)
                caminoY.append(nodoNuevo.y)
                xA=nodoNuevo.x
                yA=nodoNuevo.y
  

        #m+=1
        #if(m==8):
         #   break
        print("---------cambio de nodo--------------")
        print("nuevoNodo en:" ,xA ,yA)

    root = Tk()
    recorrido=len(caminoX)
    tamañoB=len(nBloqueosX)
    print("el numero de nodos que recorrio fue:", recorrido)



    for r in range(0, tamañoX):
        for c in range(0, tamañoY):
            recorrer=0
            bloqueo=0
            parte=False
            while recorrer<recorrido:
                if (r+1==caminoX[recorrer] and c+1==caminoY[recorrer]):
                    print(caminoX[recorrer], 'y' , caminoY[recorrer])
                    cell = Entry(root, width=10,bg="lightgreen")
                    parte=True
                recorrer=recorrer+1
            while bloqueo<tamañoB:
                if(nBloqueosX[bloqueo]==r+1 and nBloqueosY[bloqueo]==c+1):
                    print("encontro bloqueo")
                    cell = Entry(root, width=10,bg="#E6212E")
                    parte=True
                bloqueo=bloqueo+1
            if(parte==False):
                cell = Entry(root, width=10)
            cell.grid(row=c+1, column=r+1)
            cell.insert(0,'({}, {})'.format(r+1, c+1))
    print(caminoX,caminoY)


    root.mainloop()
        
    #print("encontramos el final")
            

def mostrar():
    global xI
    global yI
    global tamañoX
    global tamañoY
    global xF
    global yF
    global xA
    global yA

    print(tamañoX,tamañoY,xI,yI,xF,yF,xA,yA)
    

def actualizarI():
    global xI
    global yI
    dato = InicioX.get()
    dato2= InicioY.get()
    xI=int(dato)
    yI=int(dato2)
    print("actualizo")
    mostrar()
    nuevo()
    print("paso")


def actualizarF():
    global xF
    global yF
    dato = finalX.get()
    dato2= finalY.get()
    xF=int(dato)
    yF=int(dato2)
    print("actualizo")
    mostrar()
    nuevo()
    #print("paso")

def agregarB():
    global bloqueoX
    global bloqueoY
    dato = bloqueoX.get()
    dato2= bloqueoY.get()
    nBloqueosX.append(int(dato))
    nBloqueosY.append(int(dato2))
    print("actualizo")
    mostrar()
    nuevo()
    print("paso")

def actualizarT():
    global tamañoX
    global tamañoY
    dato = tamañoNx.get()
    dato2= tamañoNy.get()
    tamañoX=int(dato)
    tamañoY=int(dato2)
    print("actualizo")
    mostrar()
    nuevo()
    print("paso")







def crear():
    nodos=[]
    nodo=Nodo(None,None,None,None)
    nodos.append(nodo)
    nodo.padre="ya tengo un hijo"
    print(nodo.hijo)

def validar_numero(texto):
    # Esta función se llama cada vez que se ingresa texto en el cuadro de entrada
    # Verifica si el texto ingresado es un número
    if texto.isdigit() or (texto.startswith('-') and texto[1:].isdigit()):
        return True
    else:
        return False




ventana = Tk()
ventana.geometry( "740x480" )
ventana.title("Algoitmo Estrella")
boton = ttk.Button(text="Resolver camino" ,command=encontrarCamino )
botonUpdateWay = ttk.Button(text="Actualizar tamaño" ,command=actualizarT)
botonBloqueo = ttk.Button(text="Agregar Bloqueo" , command=agregarB) # actualiza el tamaño de x y y 
botonInicio = ttk.Button(text="Elegir inicio",command=actualizarI)
botonFinal = ttk.Button(text="Elegir final",command=actualizarF)

texto=ttk.Label(ventana,text="----Resuelve el algoritmo de estrella ----")
texto2=ttk.Label(ventana,text="Bienvenido a mi programa, resuelve el algoritmo de estrella")
texto3=ttk.Label(ventana,text="de manera preterminada, resuelve un cuadro 4x4 con inicio en (1,4) y fin en (4,4), con bloqueos en (3,2),(3,3) y (3,4)")
texto4=ttk.Label(ventana,text="si desea cambiar posciones de inicio y final, ademas de tamaño y bloqueos, agreguelos manualmente")
texto5=ttk.Label(ventana,text="al actualizar alguna de las variables, los bloqueos preterminados se eliminaran.")


textoX=ttk.Label(ventana,text="tamaño de las X:")
textoY=ttk.Label(ventana,text="tamaño de las Y:")

textoB=ttk.Label(ventana,text="Bloqueos")
textoBx=ttk.Label(ventana,text="X:")
textoBy=ttk.Label(ventana,text="Y:")

textoInicio=ttk.Label(ventana,text="Inicio")
textoIx=ttk.Label(ventana,text="X:")
textoIy=ttk.Label(ventana,text="Y:")

textoFinal=ttk.Label(ventana,text="Final")
textoFx=ttk.Label(ventana,text="X:")
textoFy=ttk.Label(ventana,text="Y:")

tamañoNx = tk.Entry(ventana, validate="key")
validacion = ventana.register(validar_numero)
tamañoNx.config(validatecommand=(validacion, "%P"))

tamañoNy= tk.Entry(ventana, validate="key")
tamañoNy.config(validatecommand=(validacion, "%P"))

bloqueoX = tk.Entry(ventana, validate="key")
bloqueoX.config(validatecommand=(validacion, "%P"))

bloqueoY= tk.Entry(ventana, validate="key")
bloqueoY.config(validatecommand=(validacion, "%P"))
#crea los espacios para inicios
InicioX = tk.Entry(ventana, validate="key")
InicioX.config(validatecommand=(validacion, "%P"))
InicioY= tk.Entry(ventana, validate="key")
InicioY.config(validatecommand=(validacion, "%P"))

finalX = tk.Entry(ventana, validate="key")
finalX.config(validatecommand=(validacion, "%P"))
finalY= tk.Entry(ventana, validate="key")
finalY.config(validatecommand=(validacion, "%P"))




botonUpdateWay.place(x=110,y=170)
boton.place(x=310,y=300)
botonBloqueo.place(x=285,y=170)
botonInicio.place(x=440,y=170)
botonFinal.place(x=595,y=170)
texto.place(x=260,y=10)
texto2.place(x=210,y=30)
texto3.place(x=60,y=50)
texto4.place(x=101,y=70)
texto5.place(x=145,y=90)

textoX.place(x=10,y=130)
textoY.place(x=10,y=150)
tamañoNx.place(x=100,y=130)
tamañoNy.place(x=100,y=150)

textoB.place(x=270,y=110)
textoBx.place(x=270,y=130)
textoBy.place(x=270,y=150)
bloqueoX.place(x=285,y=130)
bloqueoY.place(x=285,y=150)


textoInicio.place(x=425,y=110)
textoIx.place(x=425,y=130)
textoIy.place(x=425,y=150)
InicioX.place(x=440,y=130)
InicioY.place(x=440,y=150)

textoFinal.place(x=580,y=110)
textoIx.place(x=580,y=130)
textoIy.place(x=580,y=150)
finalX.place(x=595,y=130)
finalY.place(x=595,y=150)





ventana.mainloop()