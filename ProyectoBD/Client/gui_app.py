import tkinter as tk
from tkinter import Button
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
        barra_menu.add_cascade(label='Agente', menu=menu_agente)
        menu_agente.add_command(label='CRUD Agente')
        menu_agente.add_command(label='CRUD Propiedades')
        menu_agente.add_command(label='Propiedades Disponibles')
        menu_agente.add_command(label='Propiedades Vendidas')
        menu_agente.add_command(label='Lista Vendedores')
        menu_agente.add_command(label='Lista Compradores')
        menu_agente.add_separator()
        #menu_agente.add_command(label='Cerrar sesión', command=lambda: mostrar_login(root))
        menu_agente.add_command(label='salir', command=root.destroy)
        # Agrega más opciones según tus necesidades
    elif vista == 'vendedor':
        menu_vendedor = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Vendedor', menu=menu_vendedor)
        menu_vendedor.add_command(label='Ver Propiedades Disponibles', command=frame.tabla_propiedades_disponibles)
        menu_vendedor.add_command(label='Ver Ventas Realizadas')
        menu_vendedor.add_separator()
        menu_vendedor.add_command(label='salir', command=root.destroy)
    elif vista == 'comprador':
        menu_comprador = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Comprador', menu=menu_comprador)
        menu_comprador.add_command(label='Propiedades Disponibles')
        menu_comprador.add_command(label='Compras Realizadas')
        menu_comprador.add_separator()
        menu_comprador.add_command(label='salir', command=root.destroy)



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
        self.button_editar = tk.Button(self, text='Editar', command=self.editar)
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', 
                                  activebackground='#88dc65', )
        self.button_editar.grid(row=7, column=0, padx=10, pady=10)
        
        #Boton_Borrar
        self.button_Borrar = tk.Button(self, text='Borrar')
        self.button_Borrar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', 
                                  activebackground='#88dc65', command=self.eliminar)
        self.button_Borrar.grid(row=7, column=1, padx=10, pady=10)
    
        

    def mostrar_campos_vendedor(self):
        for widget in self.winfo_children():
            widget.destroy()
        configurar_barra_menu(self.root, 'vendedor')
        
    def mostrar_campos_comprador(self):
        for widget in self.winfo_children():
            widget.destroy()
        configurar_barra_menu(self.root, 'comprador')
        
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
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor() 
        # Obtener los datos de la tabla
        cursor.callproc("crear_agente", [self.mi_nombre.get(), self.mi_direccion.get(), int(self.mi_celular.get()), int(self.mi_telefono_Oficina.get())])
        conexion.commit()
        self.tabla_agente()
        self.deshabilitar_campos()
    
    def eliminar(self):
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor() 
        # Obtener los datos de la tabla
        seleccion = self.tabla.selection()
        valores=None
        if seleccion: 
            for item in seleccion:
                valores = self.tabla.item(item)['values']
        cursor.callproc("eliminar_agente", [int(valores[0])])
        conexion.commit()
        self.tabla_agente()

    def editar(self):
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor() 

        # Obtener los datos de la tabla
        seleccion = self.tabla.selection()

        # Verificar si se seleccionó un agente
        if not seleccion:
           print("Por favor, seleccione un agente para editar.")
           return

        # Obtener los valores del agente seleccionado
        item = seleccion[0]  # Solo necesitamos el primer elemento de la selección
        valores = self.tabla.item(item, 'values')

        # Actualizar los campos de entrada de texto con los valores actuales del agente
        self.mi_nombre.set(valores[1])
        self.mi_direccion.set(valores[2])
        self.mi_celular.set(valores[3])
        self.mi_telefono_Oficina.set(valores[4])

        # Establecer el estado de los Entry widgets como 'normal'
        self.entry_nombre.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_celular.config(state='normal')
        self.entry_telefono_Oficina.config(state='normal')


        # Definir una función de callback para la edición real de los datos
        def editar_agente():
            nuevos_nombre = self.mi_nombre.get()  
            nueva_direccion = self.mi_direccion.get()  
            nuevo_celular_str = self.mi_celular.get()  
            nuevo_telefono_oficina_str = self.mi_telefono_Oficina.get()

            # Verificar si los valores han cambiado desde la última edición
            if (
                nuevos_nombre != valores[1]
                or nueva_direccion != valores[2]
                or nuevo_celular_str != valores[3]
                or nuevo_telefono_oficina_str != valores[4]
            ): 
                # Activar el botón de confirmación si se han realizado cambios
                boton_confirmar.config(state="normal")
            else:
                    # Desactivar el botón de confirmación si no se han realizado cambios
                    boton_confirmar.config(state="disabled")  

            # Verificar si los campos requeridos están vacíos
            if not nuevos_nombre or not nueva_direccion or not nuevo_celular_str or not nuevo_telefono_oficina_str:
              print("Por favor, complete todos los campos para editar el agente.")
              return

            # Verificar si el número de celular y el teléfono de oficina son válidos
            try:
                nuevo_celular = int(nuevo_celular_str)
                nuevo_telefono_oficina = int(nuevo_telefono_oficina_str)
            except ValueError:
                print("El número de celular y el teléfono de oficina deben ser valores numéricos.")
                return

            # Llamada al procedimiento almacenado para modificar el agente
            cursor.callproc("modificar_agente", [int(valores[0]), nuevos_nombre, nueva_direccion, nuevo_celular, nuevo_telefono_oficina])

            conexion.commit()

            # Actualizar la fila seleccionada en la tabla tkinter con los nuevos valores del agente
            self.tabla.item(item, values=(valores[0], nuevos_nombre, nueva_direccion, nuevo_celular, nuevo_telefono_oficina))

            # Desactivar el botón de confirmación después de la edición
            boton_confirmar.config(state="disabled")

            # Actualizar la tabla para mostrar los cambios
            self.tabla_agente()

        # Definir un botón de confirmación para editar el agente con los nuevos valores
        boton_confirmar = tk.Button(self.root, text="Confirmar Edición", command=editar_agente)
        boton_confirmar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2',
                               activebackground='#88dc65' )
        boton_confirmar.pack(side="top", padx=10, pady=10)

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

        configurar_barra_menu(self.root, 'agente')
        #Label's
        self.label_nombre_propiedad = tk.Label(self, text='Nombre: ')
        self.label_nombre_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_nombre_propiedad.grid(row=0, column=0, padx=6, pady=10)

        self.label_ciudad_propiedad = tk.Label(self, text='Ciudad: ')
        self.label_ciudad_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_ciudad_propiedad.grid(row=1, column=0, padx=6, pady=10)

        self.label_direccion_propiedad = tk.Label(self, text='Direccion: ')
        self.label_direccion_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_direccion_propiedad.grid(row=2, column=0, padx=6, pady=10)

        self.label_dormitorios_propiedad = tk.Label(self, text='Cantidad Dormitorios: ')
        self.label_dormitorios_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_dormitorios_propiedad.grid(row=3, column=0, padx=6, pady=10)

        self.label_caracteristicas_propiedad = tk.Label(self, text='Características: ')
        self.label_caracteristicas_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_caracteristicas_propiedad.grid(row=4, column=0, padx=6, pady=10)

        self.label_precio_propiedad = tk.Label(self, text='Precio: ')
        self.label_precio_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_precio_propiedad.grid(row=5, column=0, padx=6, pady=10)

        self.label_fecha_publicacion_propiedad = tk.Label(self, text='Fecha de Publicación: ')
        self.label_fecha_publicacion_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_fecha_publicacion_propiedad.grid(row=0, column=2, padx=6, pady=10)

        self.label_agente_id_propiedad = tk.Label(self, text='ID del Agente: ')
        self.label_agente_id_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_agente_id_propiedad.grid(row=1, column=2, padx=6, pady=10)

        self.label_vendedor_id_propiedad = tk.Label(self, text='ID del Vendedor: ')
        self.label_vendedor_id_propiedad.config(font=('Arial', 12, 'bold'))
        self.label_vendedor_id_propiedad.grid(row=2, column=2, padx=6, pady=10)

    # Entrys de campo
        self.mi_nombre_propiedad = tk.StringVar()
        self.entry_nombre_propiedad = tk.Entry(self, textvariable=self.mi_nombre_propiedad)
        self.entry_nombre_propiedad.config(width=50, font=('Arial', 12))
        self.entry_nombre_propiedad.grid(row=0, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_ciudad_propiedad = tk.StringVar()
        self.entry_ciudad_propiedad = tk.Entry(self, textvariable=self.mi_ciudad_propiedad)
        self.entry_ciudad_propiedad.config(width=50, font=('Arial', 12))
        self.entry_ciudad_propiedad.grid(row=1, column=1, padx=10, pady=10, columnspan=1
    )
            
        self.mi_direccion_propiedad = tk.StringVar()
        self.entry_direccion_propiedad = tk.Entry(self, textvariable=self.mi_direccion_propiedad)
        self.entry_direccion_propiedad.config(width=50, font=('Arial', 12))
        self.entry_direccion_propiedad.grid(row=2, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_dormitorios_propiedad = tk.IntVar()
        self.entry_dormitorios_propiedad = tk.Entry(self, textvariable=self.mi_dormitorios_propiedad)
        self.entry_dormitorios_propiedad.config(width=50, font=('Arial', 12))
        self.entry_dormitorios_propiedad.grid(row=3, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_caracteristicas_propiedad = tk.StringVar()
        self.entry_caracteristicas_propiedad = tk.Entry(self, textvariable=self.mi_caracteristicas_propiedad)
        self.entry_caracteristicas_propiedad.config(width=50, font=('Arial', 12))
        self.entry_caracteristicas_propiedad.grid(row=4, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_precio_propiedad = tk.IntVar()
        self.entry_precio_propiedad = tk.Entry(self, textvariable=self.mi_precio_propiedad)
        self.entry_precio_propiedad.config(width=50, font=('Arial', 12))
        self.entry_precio_propiedad.grid(row=5, column=1, padx=10, pady=10, columnspan=1
    )

        self.mi_fecha_publicacion_propiedad = tk.StringVar()
        self.entry_fecha_publicacion_propiedad = tk.Entry(self, textvariable=self.mi_fecha_publicacion_propiedad)
        self.entry_fecha_publicacion_propiedad.config(width=50, font=('Arial', 12))
        self.entry_fecha_publicacion_propiedad.grid(row=0, column=3, padx=10, pady=10, columnspan=1
    )

        self.mi_agente_id_propiedad = tk.IntVar()
        self.entry_agente_id_propiedad = tk.Entry(self, textvariable=self.mi_agente_id_propiedad)
        self.entry_agente_id_propiedad.config(width=50, font=('Arial', 12))
        self.entry_agente_id_propiedad.grid(row=1, column=3, padx=10, pady=10, columnspan=1
    )

        self.mi_vendedor_id_propiedad = tk.IntVar()
        self.entry_vendedor_id_propiedad = tk.Entry(self, textvariable=self.mi_vendedor_id_propiedad)
        self.entry_vendedor_id_propiedad.config(width=50, font=('Arial', 12))
        self.entry_vendedor_id_propiedad.grid(row=2, column=3, padx=10, pady=10, columnspan=1
    )
        
        # Botones
        # Boton_Nuevo
        self.button_nuevo_propiedad = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo_propiedad.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2',
                                 activebackground='#88dc65', )
        self.button_nuevo_propiedad.grid(row=6, column=0, padx=10, pady=10)

        # Boton_Guardar
        self.button_guardar_propiedad = tk.Button(self, text='Guardar', command=self.guardar_datos_propiedad)
        self.button_guardar_propiedad.config(width=20, font=('Arial', 12, 'bold', ), fg='black', bg='yellow', cursor='hand2',
                                    activebackground='#88dc65', )
        self.button_guardar_propiedad.grid(row=6, column=1, padx=10, pady=10)

        # Boton_Cancelar
        self.button_cancelar_propiedad = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar_propiedad.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2',
                                     activebackground='#88dc65', )
        self.button_cancelar_propiedad.grid(row=6, column=2, padx=10, pady=10)

        # Boton_Editar
        self.button_editar_propiedad = tk.Button(self, text='Editar')
        self.button_editar_propiedad.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2',
                                   activebackground='#88dc65', command=self.editar_propiedad)
        self.button_editar_propiedad.grid(row=8, column=0, padx=10, pady=10)

        # Boton_Borrar
        self.button_Borrar = tk.Button(self, text='Borrar')
        self.button_Borrar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='#88dc65', command=self.eliminar_propiedad)
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
                self.crud_Propiedades()
            elif nivel_acceso == '2':
                self.mostrar_campos_vendedor()
            elif nivel_acceso == '3':
                self.mostrar_campos_comprador()
        else:
           print("La consulta no devolvió resultados.")

    def habilitar_campos_propiedad(self):
        # Habilitar los Entry widgets para la propiedad
        self.entry_nombre_propiedad.config(state='normal')
        self.entry_ciudad_propiedad.config(state='normal')
        self.entry_direccion_propiedad.config(state='normal')
        self.entry_dormitorios_propiedad.config(state='normal')
        self.entry_caracteristicas_propiedad.config(state='normal')
        self.entry_precio_propiedad.config(state='normal')
        self.entry_fecha_publicacion_propiedad.config(state='normal')
        self.entry_agente_id_propiedad.config(state='normal')
        self.entry_vendedor_id_propiedad.config(state='normal')

    def deshabilitar_campos_propiedad(self):
        # Deshabilitar los Entry widgets para la propiedad
        self.entry_nombre_propiedad.config(state='disabled')
        self.entry_ciudad_propiedad.config(state='disabled')
        self.entry_direccion_propiedad.config(state='disabled')
        self.entry_dormitorios_propiedad.config(state='disabled')
        self.entry_caracteristicas_propiedad.config(state='disabled')
        self.entry_precio_propiedad.config(state='disabled')
        self.entry_fecha_publicacion_propiedad.config(state='disabled')
        self.entry_agente_id_propiedad.config(state='disabled')
        self.entry_vendedor_id_propiedad.config(state='disabled')

    def guardar_datos_propiedad(self):
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor() 
        # Obtener los datos de la tabla
        cursor.callproc("CrearPropiedadEnMercado", [
        self.mi_nombre_propiedad.get(), 
        self.mi_ciudad_propiedad.get(), 
        self.mi_direccion_propiedad.get(), 
        int(self.mi_dormitorios_propiedad.get()), 
        self.mi_caracteristicas_propiedad.get(), 
        int(self.mi_precio_propiedad.get()), 
        self.mi_fecha_publicacion_propiedad.get(), 
        int(self.mi_agente_id_propiedad.get()),
        int(self.mi_vendedor_id_propiedad.get())
    ])
        conexion.commit()
        self.tabla_propiedades_disponibles()
        self.deshabilitar_campos_propiedad()

    def eliminar_propiedad(self):
        conexion = db.conexion

        # Crear un cursor
        cursor = conexion.cursor() 
        # Obtener los datos de la tabla
        seleccion = self.tabla_propiedades.selection()
        valores = None
        if seleccion: 
           for item in seleccion:
               valores = self.tabla_propiedades.item(item)['values']
        cursor.callproc("EliminarPropiedadEnMercado", [int(valores[0])])
        conexion.commit()
        self.tabla_propiedades_disponibles()


    def editar_propiedad(self):
        conexion = db.conexion
        cursor = conexion.cursor() 

        # Obtener los datos de la tabla
        seleccion = self.tabla_propiedades.selection()

        # Verificar si se seleccionó una propiedad
        if not seleccion:
           print("Por favor, seleccione una propiedad para editar.")
           return

        # Obtener los valores de la propiedad seleccionada
        item = seleccion[0]  # Solo necesitamos el primer elemento de la selección
        valores = self.tabla_propiedades.item(item, 'values')

        # Actualizar los campos de entrada de texto con los valores actuales de la propiedad
        self.mi_nombre_propiedad.set(valores[1])
        self.mi_ciudad_propiedad.set(valores[2])
        self.mi_direccion_propiedad.set(valores[3])
        self.mi_dormitorios_propiedad.set(valores[4])
        self.mi_caracteristicas_propiedad.set(valores[5])
        self.mi_precio_propiedad.set(valores[6])
        self.mi_fecha_publicacion_propiedad.set(valores[7])
        self.mi_agente_id_propiedad.set(valores[8])
        self.mi_vendedor_id_propiedad.set(valores[9])

        # Establecer el estado de los Entry widgets como 'normal'
        self.entry_nombre_propiedad.config(state='normal')
        self.entry_ciudad_propiedad.config(state='normal')
        self.entry_direccion_propiedad.config(state='normal')
        self.entry_dormitorios_propiedad.config(state='normal')
        self.entry_caracteristicas_propiedad.config(state='normal')
        self.entry_precio_propiedad.config(state='normal')
        self.entry_fecha_publicacion_propiedad.config(state='normal')
        self.entry_agente_id_propiedad.config(state='normal')
        self.entry_vendedor_id_propiedad.config(state='normal')

        def editar_propiedad_real():
            nuevos_nombre_propiedad = self.mi_nombre_propiedad.get()  
            nueva_ciudad_propiedad = self.mi_ciudad_propiedad.get()  
            nueva_direccion_propiedad = self.mi_direccion_propiedad.get()  
            nueva_dormitorios_propiedad = self.mi_dormitorios_propiedad.get()  
            nueva_caracteristicas_propiedad = self.mi_caracteristicas_propiedad.get()  
            nuevo_precio_propiedad_str = self.mi_precio_propiedad.get()  
            nueva_fecha_publicacion_propiedad = self.mi_fecha_publicacion_propiedad.get()  
            nuevo_agente_id_propiedad_str = self.mi_agente_id_propiedad.get()  
            nuevo_vendedor_id_propiedad_str = self.mi_vendedor_id_propiedad.get()

            # Verificar si los valores han cambiado desde la última edición
            if (
                nuevos_nombre_propiedad != valores[1]
                or nueva_ciudad_propiedad != valores[2]
                or nueva_direccion_propiedad != valores[3]
                or nueva_dormitorios_propiedad != valores[4]
                or nueva_caracteristicas_propiedad != valores[5]
                or nuevo_precio_propiedad_str != valores[6]
                or nueva_fecha_publicacion_propiedad != valores[7]
                or nuevo_agente_id_propiedad_str != valores[8]
                or nuevo_vendedor_id_propiedad_str != valores[9]
            ):
                
                    # Activar el botón de confirmación si se han realizado cambios
                boton_confirmar_propiedad.config(state="normal")
            else:
                    # Desactivar el botón de confirmación si no se han realizado cambios
                boton_confirmar_propiedad.config(state="disabled")  

            # Verificar si los campos requeridos están vacíos
            if not nuevos_nombre_propiedad or not nueva_ciudad_propiedad or not nueva_direccion_propiedad or not nueva_dormitorios_propiedad or not nueva_caracteristicas_propiedad or not nuevo_precio_propiedad_str or not nueva_fecha_publicacion_propiedad or not nuevo_agente_id_propiedad_str or not nuevo_vendedor_id_propiedad_str:
                print("Por favor, complete todos los campos para editar la propiedad.")
                return

            # Verificar si el precio y el tamaño de la propiedad son válidos
            try:
                nuevo_precio_propiedad = int(nuevo_precio_propiedad_str)
                nuevo_agente_id_propiedad = int(nuevo_agente_id_propiedad_str)
                nuevo_vendedor_id_propiedad = int(nuevo_vendedor_id_propiedad_str)
            except ValueError:
                print("El precio y los IDs de agente y vendedor deben ser valores numéricos.")
                return

            # Llamada al procedimiento almacenado para modificar la propiedad
            cursor.callproc("ModificarPropiedadEnMercado", [
            int(valores[0]), 
            nuevos_nombre_propiedad, 
            nueva_ciudad_propiedad, 
            nueva_direccion_propiedad, 
            nueva_dormitorios_propiedad, 
            nueva_caracteristicas_propiedad, 
            nuevo_precio_propiedad, 
            nueva_fecha_publicacion_propiedad, 
            nuevo_agente_id_propiedad, 
            nuevo_vendedor_id_propiedad
            ])

            conexion.commit()

            # Actualizar la fila seleccionada en la tabla tkinter con los nuevos valores de la propiedad
            self.tabla_propiedades.item(item, values=(
            valores[0], 
            nuevos_nombre_propiedad, 
            nueva_ciudad_propiedad, 
            nueva_direccion_propiedad, 
            nueva_dormitorios_propiedad, 
            nueva_caracteristicas_propiedad, 
            nuevo_precio_propiedad, 
            nueva_fecha_publicacion_propiedad, 
            nuevo_agente_id_propiedad, 
            nuevo_vendedor_id_propiedad
        ))

            # Desactivar el botón de confirmación después de la edición
            boton_confirmar_propiedad.config(state="disabled")
        
            # Actualizar la tabla para mostrar los cambios
            self.tabla_propiedades_disponibles()

        # Definir un botón de confirmación para editar la propiedad con los nuevos valores
        boton_confirmar_propiedad = tk.Button(self.root, text="Confirmar Edición", command=editar_propiedad_real)
        boton_confirmar_propiedad.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2',
                                activebackground='#88dc65' )
        boton_confirmar_propiedad.pack(side="top", padx=10, pady=10)


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
        self.tabla_propiedades = ttk.Treeview(self, columns=columnas)
        self.tabla_propiedades.grid(row=7, column=0, columnspan=4)

        # Configurar los encabezados de la tabla de Tkinter
        self.tabla_propiedades['columns'] = columnas
        for columna in columnas:
            self.tabla_propiedades.heading(columna, text=columna)
            self.tabla_propiedades.column(columna, width=110, anchor=tk.W)

    # Insertar los datos en la tabla de Tkinter
        for registro in datos:
            self.tabla_propiedades.insert('', 'end', values=registro)

        # Cerrar el cursor
        cursor.close()
