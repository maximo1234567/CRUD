from tkinter import *
from tkinter import ttk
#from comnexion import *
import requests


ventana=Tk()
ventana.title("Crud MySql Tkinter")
ventana.geometry("600x500")

#db=DataBase()
modificar= False
dni=StringVar()
sexo=StringVar()
nombres=StringVar()
apellidos=StringVar()
id=StringVar()

def seleccionar(event):
    id= tvEstudiantes.selection()[0]
    if int(id)>0:
        dni.set(tvEstudiantes.item(id, "values")[1])
        sexo.set(tvEstudiantes.item(id, "values")[2])
        nombres.set(tvEstudiantes.item(id, "values")[3])
        apellidos.set(tvEstudiantes.item(id, "values")[4])


marco= LabelFrame(ventana, text="Formulario de gestion de Estudiantes")
marco.place (x=50,y=50, width=500, height=400)

# labels y entrys
lblDni=Label(marco, text="DNI").grid(column=0, row=0, padx=5, pady=5)
txtDni=Entry(marco, textvariable=dni)
txtDni.grid(column=1, row=0)

lblSexo=Label(marco, text="Sexo").grid(column=0, row=1, padx=5, pady=5)
txtSexo=ttk.Combobox(marco, values=["M","F"] , textvariable=sexo)
txtSexo.grid(column=1, row=1)
txtSexo.current(0)

lblNombres=Label(marco, text="Nombres").grid(column=2, row=0, padx=5, pady=5)
txtNombres=Entry(marco, textvariable=nombres)
txtNombres.grid(column=3, row=0)

lblApellidos=Label(marco, text="Apellidos").grid(column=2, row=1, padx=5, pady=5)
txtApellidos=Entry(marco, textvariable=apellidos)
txtApellidos.grid(column=3, row=1)

lblId=Label(marco, text="id").grid(column=3, row=2, padx=6, pady=6)
txtId=Entry(marco, textvariable=id)
txtId.grid(column=4, row=2)

lblMensaje=Label(marco, text="Aqui van los mensajes", fg="green")
lblMensaje.grid(column=0, row=2, columnspan=4)

#tabla
tvEstudiantes=ttk.Treeview(marco, selectmode=NONE)

tvEstudiantes["columns"]=("ID", "DNI", "SEXO","NOMBRES","APELLIDOS",)
tvEstudiantes.column("#0", width=0, stretch=NO)
tvEstudiantes.column("ID", width=50, anchor=CENTER)
tvEstudiantes.column("DNI", width=50, anchor=CENTER)
tvEstudiantes.column("SEXO", width=50, anchor=CENTER)
tvEstudiantes.column("NOMBRES", width=100, anchor=CENTER)
tvEstudiantes.column("APELLIDOS", width=100, anchor=CENTER)
tvEstudiantes.heading("#0", text="")
tvEstudiantes.heading("ID", text="ID", anchor=CENTER)
tvEstudiantes.heading("DNI", text="DNI", anchor=CENTER)
tvEstudiantes.heading("SEXO", text="SEXO", anchor=CENTER)
tvEstudiantes.heading("NOMBRES", text="NOMBRES", anchor=CENTER)
tvEstudiantes.heading("APELLIDOS", text="APELLIDOS", anchor=CENTER)
tvEstudiantes.grid(column=0, row=3, columnspan=4)
tvEstudiantes.bind("<<TreeviewSelect>>", seleccionar)

# botones
btnEliminar=Button(marco, text="Eliminar", command=lambda:eliminar())
btnEliminar.grid(column=1, row=4)
btnNuevo=Button(marco, text="Guardar", command=lambda:nuevo())
btnNuevo.grid(column=2, row=4)
btnModificar=Button(marco, text="Seleccionar", command=lambda:actualizar())
btnModificar.grid(column=3, row=4)

#funciones
def modificarFalse():
    global modificar
    modificar=False
    tvEstudiantes.config(selectmode=NONE)
    btnNuevo.config(text="Guardar")
    btnModificar.config(text="Seleccionar")
    btnEliminar.config(state=DISABLED)
def modificarTrue():
    global modificar
    modificar=True
    tvEstudiantes.config(selectmode=BROWSE)
    btnNuevo.config(text="Nuevo")
    btnModificar.config(text="Modificar")
    btnEliminar.config(state=NORMAL)

def validar():
    return len(dni.get()) and len(nombres.get()) and len(apellidos.get())

def limpiar():
    dni.set("")
    nombres.set("")
    apellidos.set("")
    
def vaciar_tabla():
    filas= tvEstudiantes.get_children()
    for fila in filas:
        tvEstudiantes.delete(fila)
        
def llenar_tabla():
    vaciar_tabla()

    str_url = "http://g1.pwd.tecnica4berazategui.edu.ar/mostrar.php"
    response = requests.get(str_url)

    if response.status_code == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        data = response.json()

        for row in data:
            id = row["id"]
            dni_val = row["dni"]
            sexo_val = row["sexo"]
            nombres_val = row["nombres"]
            apellidos_val = row["apellidos"]

            tvEstudiantes.insert("", END, id, values=(id, dni_val, sexo_val, nombres_val, apellidos_val))
    else:
        lblMensaje.config(text= response.status_code, fg="red")

        
def eliminar():
    id_a_eliminar = txtId.get()
    if id_a_eliminar and int(id_a_eliminar) > 0:
        
        str_url = "http://g1.pwd.tecnica4berazategui.edu.ar/eliminar.php?id=" + id_a_eliminar
        requests.get(str_url)

        tvEstudiantes.delete(id_a_eliminar)
        lblMensaje.config(text="Se ha eliminado el registro correctamente")
        limpiar()
        llenar_tabla()
    else:
        lblMensaje.config(text="Ingrese un ID válido para eliminar", fg="red")
    
        
def nuevo():
    if modificar==False:
        if validar():
            val=(dni.get(),sexo.get(),nombres.get(),apellidos.get())
            str_url="http://g1.pwd.tecnica4berazategui.edu.ar/alta_bd.php?dni="+dni.get()+"&sexo="+sexo.get()+"&nombres="+nombres.get()+"&apellidos="+apellidos.get()
            requests.get(str_url)
            lblMensaje.config(text="Se guardo un registro correctamente", fg="green")
            llenar_tabla()
            limpiar()
        else:
            lblMensaje.config(text="Los campos no tienen que quedar vacio", fg="red")
    else:
        modificarFalse()
def actualizar():
    if modificar == True:
        if validar():
            id_seleccionado = txtId.get()

            if not id_seleccionado.isdigit():
                lblMensaje.config(text="Ingrese un ID válido para actualizar", fg="red")
                return

            val = (dni.get(), sexo.get(), nombres.get(), apellidos.get())
            sql = "update estudiantes set dni=%s, sexo=%s, nombres=%s, apellidos=%s where id=" + id_seleccionado

            str_url = f"http://g1.pwd.tecnica4berazategui.edu.ar/update.php?id={id_seleccionado}&dni={dni.get()}&sexo={sexo.get()}&nombres={nombres.get()}&apellidos={apellidos.get()}"
            requests.get(str_url)

            lblMensaje.config(text="Se actualizó el registro correctamente", fg="green")
            llenar_tabla()
            limpiar()
        else:
            lblMensaje.config(text="Los campos no deben quedar vacíos", fg="red")
    else:
        modificarTrue()

llenar_tabla()
ventana.mainloop()