import tkinter as tk
from Client.gui_app import Frame, configurar_barra_menu

def main():
    root = tk.Tk()
    root.title('Proyecto BD')
    root.iconbitmap('img/Casa.ico')
    
    
    
    app = Frame(root = root)
    configurar_barra_menu(root, 'login')
    app.mainloop()

if __name__ == '__main__':
    main()