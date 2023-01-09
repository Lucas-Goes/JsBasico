import tkinter as tk
import tkinter.messagebox
import customtkinter
import time

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

global lista
lista = ['Teste']

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{500}x{480}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="TESTE TESTE", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # create tabview
        self.options_window = customtkinter.CTkButton(self.sidebar_frame, text="Opções",command=self.create_toplevel)
        self.options_window.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.options_window2 = customtkinter.CTkButton(self.sidebar_frame, text="Chama Log",command=self.lista_log)
        self.options_window2.grid(row=3, column=0, padx=20, pady=(10, 10))



    def lista_log(self):
        lista.append('Android')
        lista.pop(0)
        #lista.insert(0,'Oracle')

    def create_toplevel(self):
        
        def log_processamento():
            window.textbox.insert("0.0", str(lista) + "\n\n")
            window.textbox.focus_set()
         
        self.options_window.configure(state="disabled")
        window = customtkinter.CTkToplevel(self)
        window.geometry("280x480")
         # configure grid layout (4x4)
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure((0, 0), weight=0)
        window.grid_rowconfigure((4, 4, 4), weight=1)

        window.options_window = customtkinter.CTkButton(window, text="Opções",command=log_processamento)
        window.options_window.grid(row=1, column=0, padx=20, pady=(10, 10))
        window.title("Processando...")
        window.progressbar_1 = customtkinter.CTkProgressBar(window)
        window.progressbar_1.grid(row=2, column=0, padx=(20, 10), pady=(50, 10), sticky="ew")
        window.textbox = customtkinter.CTkTextbox(window, width=250, height=315)
        window.textbox.grid(row=3, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def on_close():
            self.options_window.configure(state="normal")
            window.destroy()
        
        window.protocol("WM_DELETE_WINDOW", on_close)


if __name__ == "__main__":
    app = App()
    app.mainloop()