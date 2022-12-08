from tkinter import *  
from requestPI import obtenerPrendas

prendas = []

def clickBoton():
    for item in listbox.curselection():
        item = listbox.get(item)
    texto = obtenerPrendas(item)
    imprimirTexto(texto)
    return

def imprimirTexto(texto):
    for i in range(len(texto)):
        prenda = texto[i]['PRENDA']
        unidades = texto[i]['UNIDADES']
        textoMostrar = prenda + ': ' + str(unidades) + " "
        textoMostrar = str(textoMostrar) 
        if (i==0):
            a = textoMostrar + "\n";
        else:
            a = a + textoMostrar + "\n"

    display_text.set(a)


ventana = Tk()
ventana.geometry("300x300")
etiqueta = Label(ventana, text="Calculadora de inventario")
etiqueta.pack()


BotonCalcularInventario = Button(ventana,text="ENTER",command= clickBoton)
BotonCalcularInventario.pack()

#listbox
listbox = Listbox(ventana)   
listbox.insert(1,"ARKADIA")  
listbox.insert(2, "COMPRETEX ECOMMERCE")  
listbox.insert(3, "GUAYABAL")  
listbox.insert(4, "LA CENTRAL")  
listbox.insert(5,"MARINILLA")  
listbox.insert(6, "MAYORCA 1")  
listbox.insert(7, "MAYORCA 2")  
listbox.insert(8, "MOLINOS 1")  
listbox.insert(9,"PARQUE LA CEJA")  
listbox.insert(10, "PREMIUM PLAZA")  
listbox.insert(11, "PUERTA DEL NTE")  
listbox.insert(12, "RIONEGRO")  
listbox.insert(13,"TERMINAL DEL NORTE")  
listbox.insert(14, "VIVA ENVIGADO")  
listbox.insert(15, "PLAZA FABRICATO")  
listbox.insert(16, "RIONEGRO PARQUE")  
listbox.insert(17, "CAMINO REAL")  
listbox.pack()  
display_text = StringVar()
etiqueta2 = Label(ventana, textvariable=display_text)
#etiqueta2.place(x = 100, y = 220, width=200, height=200)
etiqueta2.pack()


ventana.mainloop()