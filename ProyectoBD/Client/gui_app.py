import tkinter as tk
import _mysql_connector
from tkinter import ttk
from model import conexion_db as db

def configurar_barra_menu(root, vista):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    if vista == 'login':
        pass

    elif vista == 'agente':
        menu_agente = tk.Menu(barra_menu, tearoff=0)
        menu_consultas = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Agente', menu=menu_agente)
        menu_agente.add_command(label='Crear Registro en BD')
        menu_agente.add_command(label='Eliminar Registro en BD')
        menu_agente.add_command(label='Editar Registro en BD')
        menu_agente.add_separator()
        #menu_agente.add_command(label='Cerrar sesión', command=lambda: mostrar_login(root))
        menu_agente.add_command(label='salir', command=root.destroy)
        barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
        # Agrega más opciones según tus necesidades
    elif vista == 'vendedor':
        menu_vendedor = tk.Menu(barra_menu, tearoff=0)
        menu_consultas = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Vendedor', menu=menu_vendedor)
        menu_vendedor.add_command(label='')
        menu_vendedor.add_command(label='Opción 2')
        menu_vendedor.add_separator()
        menu_vendedor.add_command(label='salir', command=root.destroy)
        barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
    
class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=480, height=320 )
        self.root = root
        self.pack()
        self.config(width=480, height=320, bg='white')
        
        self.mostrar_login()
    

    def mostrar_login(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        configurar_barra_menu(self.root, 'login')
        self.label_bienvenido = tk.Label(self, text='Bienvenido')
        self.label_bienvenido.config(font= ('Arial', 20, 'bold'))
        self.label_bienvenido.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.label_usuario = tk.Label(self, text='Usuario')
        self.label_usuario.config(font= ('Arial', 12, 'bold'))
        self.label_usuario.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_usuario = tk.StringVar()
        self.entry_usuario = tk.Entry(self, textvariable=self.mi_usuario)
        self.entry_usuario.config(width=50, font=('Arial', 12))
        self.entry_usuario.grid(row=2, column=1, padx=10, pady=10, columnspan= 2)
        
        self.label_password = tk.Label(self, text='Password')
        self.label_password.config(font= ('Arial', 12, 'bold'))
        self.label_password.grid(row=3, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_password = tk.StringVar()
        self.entry_password = tk.Entry(self, textvariable=self.mi_password)
        self.entry_password.config(width=50, font=('Arial', 12))
        self.entry_password.grid(row=4, column=1, padx=10, pady=10, columnspan= 2)
        
        self.button_login = tk.Button(self, text='Iniciar Sesion', command=lambda: self.validar_credenciales(self.mi_usuario.get(), self.mi_password.get()))
        self.button_login.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_login.grid(row=5, column=0, padx=10, pady=10, columnspan=4)
            
    def mostrar_campos_agente(self):
        for widget in self.winfo_children():
            widget.destroy()
        configurar_barra_menu(self.root, 'agente')

        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font= ('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_direccion = tk.Label(self, text='Direccion: ')
        self.label_direccion.config(font= ('Arial', 12, 'bold'))
        self.label_direccion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_Celular = tk.Label(self, text='Celular: ')
        self.label_Celular.config(font= ('Arial', 12, 'bold'))
        self.label_Celular.grid(row=2, column=0, padx=10, pady=10)
        
        self.label_Tel_Oficina = tk.Label(self, text='Telefono Oficina: ')
        self.label_Tel_Oficina.config(font= ('Arial', 12, 'bold'))
        self.label_Tel_Oficina.grid(row=3, column=0, padx=10, pady=10)
        
        #Entrys de campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable=self.mi_direccion)
        self.entry_direccion.config(width=50, font=('Arial', 12))
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_celular = tk.StringVar()
        self.entry_celular = tk.Entry(self, textvariable=self.mi_celular)
        self.entry_celular.config(width=50, font=('Arial', 12))
        self.entry_celular.grid(row=2, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_telefono_Oficina = tk.StringVar()
        self.entry_telefono_Oficina = tk.Entry(self, textvariable=self.mi_telefono_Oficina)
        self.entry_telefono_Oficina.config(width=50, font=('Arial', 12))
        self.entry_telefono_Oficina.grid(row=3, column=1, padx=10, pady=10, columnspan= 2)
        
        #Botones
        #Boton_Nuevo
        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_nuevo.grid(row=5, column=0, padx=10, pady=10)
        
        #Boton_Guardar
        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='yellow', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_guardar.grid(row=5, column=1, padx=10, pady=10)
        
        #Boton_Cancelar
        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_cancelar.grid(row=5, column=2, padx=10, pady=10)
        
        self.deshabilitar_campos()
        self.tabla_agente()
        
        #Boton_Editar
        self.button_editar = tk.Button(self, text='Editar')
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_editar.grid(row=7, column=0, padx=10, pady=10)
        
        #Boton_Borrar
        self.button_Borrar = tk.Button(self, text='Borrar')
        self.button_Borrar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_Borrar.grid(row=7, column=1, padx=10, pady=10)
        
    def mostrar_campos_vendedor(self):
        for widget in self.winfo_children():
            widget.destroy()
        configurar_barra_menu(self.root, 'vendedor')
        
        
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font= ('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_direccion = tk.Label(self, text='Direccion: ')
        self.label_direccion.config(font= ('Arial', 12, 'bold'))
        self.label_direccion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_Celular = tk.Label(self, text='Celular: ')
        self.label_Celular.config(font= ('Arial', 12, 'bold'))
        self.label_Celular.grid(row=2, column=0, padx=10, pady=10)
        
        #Entrys de campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable=self.mi_direccion)
        self.entry_direccion.config(width=50, font=('Arial', 12))
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_celular = tk.StringVar()
        self.entry_celular = tk.Entry(self, textvariable=self.mi_celular)
        self.entry_celular.config(width=50, font=('Arial', 12))
        self.entry_celular.grid(row=2, column=1, padx=10, pady=10, columnspan= 2)
        
        
        #Botones
        #Boton_Nuevo
        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_nuevo.grid(row=5, column=0, padx=10, pady=10)
        
        #Boton_Guardar
        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='yellow', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_guardar.grid(row=5, column=1, padx=10, pady=10)
        
        #Boton_Cancelar
        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_cancelar.grid(row=5, column=2, padx=10, pady=10)
        
        self.deshabilitar_campos()
        self.tabla_vendedor()
        
        #Boton_Editar
        self.button_editar = tk.Button(self, text='Editar')
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_editar.grid(row=7, column=0, padx=10, pady=10)
        
        #Boton_Borrar
        self.button_Borrar = tk.Button(self, text='Borrar')
        self.button_Borrar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_Borrar.grid(row=7, column=1, padx=10, pady=10)

        self.deshabilitar_campos
        self.tabla_ventas_por_vendedor()
        
    def mostrar_campos_comprador(self):
        for widget in self.winfo_children():
            widget.destroy()
        configurar_barra_menu(self.root, 'comprador')
        
        
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font= ('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_direccion = tk.Label(self, text='Direccion: ')
        self.label_direccion.config(font= ('Arial', 12, 'bold'))
        self.label_direccion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_Celular = tk.Label(self, text='Celular: ')
        self.label_Celular.config(font= ('Arial', 12, 'bold'))
        self.label_Celular.grid(row=2, column=0, padx=10, pady=10)
        
        #Entrys de campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable=self.mi_direccion)
        self.entry_direccion.config(width=50, font=('Arial', 12))
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_celular = tk.StringVar()
        self.entry_celular = tk.Entry(self, textvariable=self.mi_celular)
        self.entry_celular.config(width=50, font=('Arial', 12))
        self.entry_celular.grid(row=2, column=1, padx=10, pady=10, columnspan= 2)
        
        
        #Botones
        #Boton_Nuevo
        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_nuevo.grid(row=5, column=0, padx=10, pady=10)
        
        #Boton_Guardar
        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='yellow', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_guardar.grid(row=5, column=1, padx=10, pady=10)
        
        #Boton_Cancelar
        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_cancelar.grid(row=5, column=2, padx=10, pady=10)
        
        self.deshabilitar_campos()
        self.tabla_comprador()
        
        #Boton_Editar
        self.button_editar = tk.Button(self, text='Editar')
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_editar.grid(row=7, column=0, padx=10, pady=10)
        
        #Boton_Borrar
        self.button_Borrar = tk.Button(self, text='Borrar')
        self.button_Borrar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_Borrar.grid(row=7, column=1, padx=10, pady=10)

        self.deshabilitar_campos
        self.tabla_compras_por_comprador()
        
    def habilitar_campos(self):
        self.mi_nombre.set(' ')
        self.mi_direccion.set(' ')
        self.mi_celular.set(' ')
        self.mi_telefono_Oficina.set(' ')
        
        self.entry_nombre.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_celular.config(state='normal')
        self.entry_telefono_Oficina.config(state='normal')
        
        self.button_guardar.config(state='normal')
        self.button_cancelar.config(state='normal')
            
    def deshabilitar_campos(self):
        self.mi_nombre.set(' ')
        self.mi_direccion.set(' ')
        self.mi_celular.set(' ')
        self.mi_telefono_Oficina.set(' ')
        
        
        
        self.entry_nombre.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.entry_celular.config(state='disabled')
        self.entry_telefono_Oficina.config(state='disabled')
        
        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def guardar_datos(self):
        self.deshabilitar_campos()
        
    def tabla_agente(self):
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor()

        # Obtener los datos de la tabla
        cursor.execute("SELECT * FROM agentes")
        datos = cursor.fetchall()

        # Crear una lista vacía para las columnas
        columnas = []

        # Obtener los nombres de las columnas
        for descripcion in cursor.description:
            columnas.append(descripcion[0])

        # Configurar la tabla de Tkinter
        self.tabla = ttk.Treeview(self, columns=columnas)
        self.tabla.grid(row=6, column=0, columnspan=4)

        # Configurar los encabezados de la tabla de Tkinter
        self.tabla['columns'] = columnas
        for columna in columnas:
            self.tabla.heading(columna, text=columna)

        # Insertar los datos en la tabla de Tkinter
        for registro in datos:
            self.tabla.insert('', 'end', values=registro)

        # Cerrar el cursor
        cursor.close()
        
    def tabla_propiedades_disponibles(self):
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor()

        # Obtener los datos de la tabla
        cursor.execute("SELECT * FROM propiedades_en_mercado")
        datos = cursor.fetchall()

        # Crear una lista vacía para las columnas
        columnas = []

        # Obtener los nombres de las columnas
        for descripcion in cursor.description:
            columnas.append(descripcion[0])

        # Configurar la tabla de Tkinter
        style = ttk.Style()
        style.configure("Treeview", bordercolor="black", borderwidth=1, relief="solid")
        self.tabla = ttk.Treeview(self, columns=columnas)
        self.tabla.grid(row=7, column=0, columnspan=4)

        # Configurar los encabezados de la tabla de Tkinter
        self.tabla['columns'] = columnas
        for columna in columnas:
            self.tabla.heading(columna, text=columna)
            self.tabla.column(columna, width=110, anchor=tk.W)

        # Insertar los datos en la tabla de Tkinter
        for registro in datos:
            self.tabla.insert('', 'end', values=registro)


        # Configurar las barras de desplazamiento con el Treeview
        #self.tabla.config(yscrollcommand=barra_scroll_vertical.set, xscrollcommand=barra_scroll_horizontal.set)

        # Cerrar el cursor
        cursor.close()
    
    def tabla_ventas_por_agente(self):
        pass
    
    def mostrar_propiedades_en_mercado(self):
        for widget in self.winfo_children():
            widget.destroy()
    
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor()

        # Obtener los datos de la tabla
        cursor.execute("SELECT * FROM ventas_por_vendedor")
        datos = cursor.fetchall()

        # Crear una lista vacía para las columnas
        columnas = []

        # Obtener los nombres de las columnas
        for descripcion in cursor.description:
            columnas.append(descripcion[0])

        # Configurar la tabla de Tkinter
        style = ttk.Style()
        style.configure("Treeview", bordercolor="black", borderwidth=1, relief="solid")
        self.tabla = ttk.Treeview(self, columns=columnas)
        self.tabla.grid(row=6, column=0, columnspan=4)

        # Configurar los encabezados de la tabla de Tkinter
        self.tabla['columns'] = columnas
        for columna in columnas:
            self.tabla.heading(columna, text=columna)
            self.tabla.column(columna, width=110, anchor=tk.W)

        # Insertar los datos en la tabla de Tkinter
        for registro in datos:
            self.tabla.insert('', 'end', values=registro)


        # Configurar las barras de desplazamiento con el Treeview
        #self.tabla.config(yscrollcommand=barra_scroll_vertical.set, xscrollcommand=barra_scroll_horizontal.set)

        # Cerrar el cursor
        cursor.close() 
        
    def crud_Propiedades(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        #Label's
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=6, pady=10)

        self.label_ciudad = tk.Label(self, text='Ciudad: ')
        self.label_ciudad.config(font=('Arial', 12, 'bold'))
        self.label_ciudad.grid(row=1, column=0, padx=6, pady=10)

        self.label_direccion = tk.Label(self, text='Direccion: ')
        self.label_direccion.config(font=('Arial', 12, 'bold'))
        self.label_direccion.grid(row=2, column=0, padx=6, pady=10)

        self.label_dormitorios = tk.Label(self, text='Cantidad Dormitorios: ')
        self.label_dormitorios.config(font=('Arial', 12, 'bold'))
        self.label_dormitorios.grid(row=3, column=0, padx=6, pady=10)

        self.label_caracteristicas = tk.Label(self, text='Características: ')
        self.label_caracteristicas.config(font=('Arial', 12, 'bold'))
        self.label_caracteristicas.grid(row=4, column=0, padx=6, pady=10)

        self.label_precio = tk.Label(self, text='Precio: ')
        self.label_precio.config(font=('Arial', 12, 'bold'))
        self.label_precio.grid(row=5, column=0, padx=6, pady=10)

        self.label_fecha_publicacion = tk.Label(self, text='Fecha de Publicación: ')
        self.label_fecha_publicacion.config(font=('Arial', 12, 'bold'))
        self.label_fecha_publicacion.grid(row=0, column=2, padx=6, pady=10)

        self.label_agente_id = tk.Label(self, text='ID del Agente: ')
        self.label_agente_id.config(font=('Arial', 12, 'bold'))
        self.label_agente_id.grid(row=1, column=2, padx=6, pady=10)

        self.label_vendedor_id = tk.Label(self, text='ID del Vendedor: ')
        self.label_vendedor_id.config(font=('Arial', 12, 'bold'))
        self.label_vendedor_id.grid(row=2, column=2, padx=6, pady=10)

    # Entrys de campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_ciudad = tk.StringVar()
        self.entry_ciudad = tk.Entry(self, textvariable=self.mi_ciudad)
        self.entry_ciudad.config(width=50, font=('Arial', 12))
        self.entry_ciudad.grid(row=1, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable=self.mi_direccion)
        self.entry_direccion.config(width=50, font=('Arial', 12))
        self.entry_direccion.grid(row=2, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_dormitorios = tk.IntVar()
        self.entry_dormitorios = tk.Entry(self, textvariable=self.mi_dormitorios)
        self.entry_dormitorios.config(width=50, font=('Arial', 12))
        self.entry_dormitorios.grid(row=3, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_caracteristicas = tk.StringVar()
        self.entry_caracteristicas = tk.Entry(self, textvariable=self.mi_caracteristicas)
        self.entry_caracteristicas.config(width=50, font=('Arial', 12))
        self.entry_caracteristicas.grid(row=4, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_precio = tk.IntVar()
        self.entry_precio = tk.Entry(self, textvariable=self.mi_precio)
        self.entry_precio.config(width=50, font=('Arial', 12))
        self.entry_precio.grid(row=5, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_fecha_publicacion = tk.StringVar()
        self.entry_fecha_publicacion = tk.Entry(self, textvariable=self.mi_fecha_publicacion)
        self.entry_fecha_publicacion.config(width=50, font=('Arial', 12))
        self.entry_fecha_publicacion.grid(row=0, column=3, padx=10, pady=10, columnspan=1
    )

        self.mi_agente_id = tk.IntVar()
        self.entry_agente_id = tk.Entry(self, textvariable=self.mi_agente_id)
        self.entry_agente_id.config(width=50, font=('Arial', 12))
        self.entry_agente_id.grid(row=1, column=3, padx=10, pady=10, columnspan=1
    )

        self.mi_vendedor_id = tk.IntVar()
        self.entry_vendedor_id = tk.Entry(self, textvariable=self.mi_vendedor_id)
        self.entry_vendedor_id.config(width=50, font=('Arial', 12))
        self.entry_vendedor_id.grid(row=2, column=3, padx=10, pady=10, columnspan=1
    )

        # Botones
        # Boton_Nuevo
        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2',
                                 activebackground='#88dc65', )
        self.button_nuevo.grid(row=6, column=0, padx=10, pady=10)

        # Boton_Guardar
        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold', ), fg='black', bg='yellow', cursor='hand2',
                                    activebackground='#88dc65', )
        self.button_guardar.grid(row=6, column=1, padx=10, pady=10)

        # Boton_Cancelar
        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2',
                                     activebackground='#88dc65', )
        self.button_cancelar.grid(row=6, column=2, padx=10, pady=10)

        # Boton_Editar
        self.button_editar = tk.Button(self, text='Editar')
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2',
                                   activebackground='#88dc65', )
        self.button_editar.grid(row=8, column=0, padx=10, pady=10)

        # Boton_Borrar
        self.button_Borrar = tk.Button(self, text='Borrar')
        self.button_Borrar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='#88dc65')
        self.button_Borrar.grid(row=8, column=1, padx=10, pady=10)

        self.tabla_propiedades_disponibles()

    def validar_credenciales(self, usuario, password):
        conexion = db.conexion


        cursor = conexion.cursor()


        query = "SELECT Nivel_Acceso FROM credenciales WHERE (Nombre_Usuario_Agentes = %s OR Nombre_Usuario_Vendedores = %s OR Nombre_Usuario_Compradores = %s) AND Password = %s"  
        valores = (usuario, usuario, usuario, password)
        cursor.execute(query, valores)

        resultado = cursor.fetchone()

        if resultado:
            nivel_acceso = resultado[0]
            if nivel_acceso == '1':
                self.mostrar_campos_agente()
            elif nivel_acceso == '2':
                self.mostrar_campos_vendedor()
            elif nivel_acceso == '3':
                self.mostrar_campos_comprador()
        else:
           print("La consulta no devolvió resultados.")


