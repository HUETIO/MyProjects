
from cgitb import text
from faulthandler import disable
from tkinter import*
from tkinter import ttk
from Conexion import *
ventana = Tk()
ventana.title("Desing Software")
ventana.geometry("1090x600")
marco=ttk.Labelframe(ventana, text="Formulario Control de Inventarios")
marco.place(x=15,y=10,width=1060,height=550)
#Clases
bd=conexion()
id1=StringVar()
id2=StringVar()
Nombres=StringVar()
Apellidos=StringVar()
Maq=StringVar()
#labelyentris

lblid1 = Label (marco,text="INGRESE ID UNICO DE IDENTIFICACION:").grid(column=0,row=0,padx=10, ipady=10)
txtid1=Entry(marco, textvariable=id1,width=30)
txtid1.grid(column=1,row=0)

lblid2 = Label (marco,text="INGRESE CEDULA O IDENTIFICACION:").grid(column=0,row=1,padx=10, ipady=10)
txtid2=Entry(marco, textvariable=id2,width=30)
txtid2.grid(column=1,row=1)

lblNombres = Label (marco,text="INGRESE UN NOMBRE:").grid(column=2,row=0,padx=10, ipady=10)
txtNombres=Entry(marco, textvariable=Nombres,width=50)
txtNombres.grid(column=3,row=0)

lblApellidos = Label (marco,text="INGRESE UN APELLIDO:").grid(column=2,row=1,padx=10, ipady=10)
txtApellidos=Entry(marco, textvariable=Apellidos,width=50)
txtApellidos.grid(column=3,row=1)

lblMaq = Label (marco,text="INGRESE LA HERRAMIENTA/MAQUINA:").grid(column=1,row=4)
txtMaq=Entry(marco, textvariable=Maq,width=50)
txtMaq.grid(column=3,row=4,ipady=30,)

txtmensaje= Label (marco,text="AQUI VA LO QUE REGISTRA  -----➤➤   ",fg="blue").grid(column=0,row=4,padx=10, ipady=10)
txtmensaje1= Label (marco,text="SELECCIONE UNA ACCION   ",fg="blue")
txtmensaje1.grid(column=0,row=6)

#aqui va la tabla de entrada
tvTablaDatosSoft=ttk.Treeview(marco)
tvTablaDatosSoft.grid(column=0,row=15,columnspan=4,padx=10)
tvTablaDatosSoft["columns"]=("id1","id2","Maq","Nombres","Apellidos")

#columnas y tablas editos
tvTablaDatosSoft.column("#0",width=0, stretch=NO)
tvTablaDatosSoft.column("id1",width=200, anchor=CENTER)
tvTablaDatosSoft.column("id2",width=200, anchor=CENTER)
tvTablaDatosSoft.column("Maq",width=200, anchor=CENTER)
tvTablaDatosSoft.column("Nombres",width=200, anchor=CENTER)
tvTablaDatosSoft.column("Apellidos",width=200, anchor=CENTER)
tvTablaDatosSoft.heading("#0",text="")
tvTablaDatosSoft.heading("id1",text="ID UNICO")
tvTablaDatosSoft.heading("id2",text="CEDULA IDENTIFICACION")
tvTablaDatosSoft.heading("Maq",text="MAQUINA O HERRAMIENTA")
tvTablaDatosSoft.heading("Nombres",text="NOMBRES")
tvTablaDatosSoft.heading("Apellidos",text="APELLIDOS")



 #Funciones
def vaciar_tabla():
   filas= tvTablaDatosSoft.get_children()
   for fila in filas:
      tvTablaDatosSoft.delete(fila)
def llenar_tabla():
   vaciar_tabla()
   sql="select * from desingtable"
   bd.cursor.execute(sql)
   filas=bd.cursor.fetchall()
   for fila in filas:
      id1=fila[0]
      tvTablaDatosSoft.insert("", END,id1,text=id1, values=fila)
   pass

def eliminar():
    id1=tvTablaDatosSoft.selection()[0]
    if int(id1) > 0:
        sql="delete from desingtable where id1="+id1
        bd.cursor.execute(sql)
        bd.connection.commit()
        tvTablaDatosSoft.delete(id1)
        txtmensaje1.config(text="SE HA ELIMINADO REGISTRO CORRECTAMENTE!")
    else:
        txtmensaje1.config(text="SELECCIONE UN REGISTRO PARA ELIMINAR!")
    pass

def modificar():
 pass
def agregar():

        val=(id1.get(),id2.get(),Nombres.get(),Apellidos.get(),Maq.get())
        sql="insert into desingtable (id1, id2, Nombres, Apellidos, Maq) values (%s, %s, %s, %s, %s)"
        bd.cursor.execute(sql, val)
        bd.connection.commit()
        txtmensaje1.config(text="SE HA CREADO REGISTRO CORRECTAMENTE!",fg="green")
       
        llenar_tabla()

def buscar():
   pass


#botenonera
#btnBuscar= Button(marco, text="Buscar Informacion", command=lambda:buscar())
#btnBuscar.grid(column=0, row=20)

btnEliminar= Button(marco, text="Eliminar Informacion", command=lambda:eliminar())
btnEliminar.grid(column=1, row=20)

btnModificar= Button(marco, text="Modificar la Informacion", command=lambda:modificar())
btnModificar.grid(column=2, row=20)

btnAgregar= Button(marco, text="Agregar nueva Informacion", command=lambda:agregar())
btnAgregar.grid(column=3, row=20)


llenar_tabla()
ventana.mainloop()

#frm = ttk.Frame(root, padding=10)
#frm.grid()
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

