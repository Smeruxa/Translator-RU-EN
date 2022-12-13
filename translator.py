from src.libraries import *
from src.class_translate import translate
from src.class_config import config
from src.class_log import log


### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa

HideWindow = True

class framework:

    global GetSystemMetrics

    text_of_area = """Waiting for text.."""
    screen_x, screen_y = GetSystemMetrics(0), GetSystemMetrics(1)

    def __init__(self, config, log):

        # create_window & configure
        self.config_table = config.get()
        self.ToEnglish = True if self.config_table['speak'] == "Русский" else False
        self.Ox, self.Oy = 396, 77
        self.clicked = False
        self.window = Window()
        self.window.root.geometry(str(self.Ox) + "x" + str(self.Oy)) # size
        self.window.root.geometry("+" + self.config_table["x"] + "+" + self.config_table["y"]) # pos
        self.window.root.configure(bg="gray")
        self.translator = translate()
        self.hide()
        # create_window & configure

        # binds
        self.window.root.bind('<Configure>', self.image_resize)
        self.window.root.bind('<ButtonRelease-1>', self.released)
        # binds

        # first_column
        self.entry = tk.Entry(self.window.root, width=25)
        self.entry.grid(row=0, column=0, pady=2)
        self.button = tk.Button(self.window.root, text="Translate", width=21, command=lambda: self.translate_callback())
        self.button.grid(row=1, column=0, pady=2)
        self.label1 = tk.Label(self.window.root, text=("Русский" if self.config_table['speak'] == "Английский" else "Английский"))
        self.label1.grid(row=2, column=0)
        # first_column

        # second_column
        button = tk.Button(self.window.root, text="<=>", width=5, command=lambda: self.change_speak()).grid(row=1, column=1, padx=5)
        # second_column

        # last_column  
        self.text_area = st.ScrolledText(self.window.root, width=20, height=4)
        self.text_area.place(x=213, y=4)
        self.text_area.insert(tk.INSERT, self.text_of_area)
        self.text_area.configure(state='disabled')
        log.add_line("The loading of the framework elements was successful.")
        # last_column

    def released(self, event):
        self.clicked = True

    def image_resize(self, event):
        global HideWindow
        if self.clicked and not HideWindow:
            self.window.root.update()
            self.config_table["x"], self.config_table["y"] = str(self.window.root.winfo_x()), str(self.window.root.winfo_y())
            config.save(self.config_table)
            log.add_line("MSG >> Window position saved successfully.")
            self.clicked = False

    def show(self):
        self.window.root.deiconify()
        self.window.root.focus_set()
    
    def hide(self):
        self.window.root.withdraw()
    def translate_callback(self):
        self.text_area.configure(state='normal')
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.INSERT, self.translator.translate(self.entry.get(), ("ru" if not self.ToEnglish else "en"), ("ru" if self.ToEnglish else "en")))
        self.text_area.configure(state='disabled')
        log.add_line("MSG >> The translation of the text was completed successfully.")

    def change_speak(self):
        self.ToEnglish = not self.ToEnglish
        self.config_table["speak"] = "Русский" if self.ToEnglish else "Английский"
        config.save(self.config_table)
        log.add_line("MSG >> The translator mode has been changed on " + self.config_table["speak"] + ".")
        self.label1.config(text=("Русский" if not self.ToEnglish else "Английский"))

def set_window_state(window):
    global HideWindow
    HideWindow = not HideWindow
    if HideWindow:
        window.hide()
        log.add_line("MSG >> The window has been hidden.")
    else:
        window.show()
        log.add_line("MSG >> The window has been enabled.")

def def_of_thread(window):
    keyboard.add_hotkey('control + shift + 1', lambda: set_window_state(window))

def end_thread(thread, log):
    thread.join()
    log.add_line("MSG >> Application completed successfully.")

def main():
    # create log
    global log
    log = log()
    log.add_line("LIBRARY >> Log was loaded.")
    # create log 
    # create config
    global config
    config = config()
    log.add_line("LIBRARY >> Config was loaded.")
    # create config
    # create framework & thread & end_thread
    Draw = framework(config, log)
    thread = Thread(target=def_of_thread, args=[Draw.window])
    thread.start()
    log.add_line("LIBRARY >> Thread has been launched.")
    atexit.register(end_thread, thread, log)
    log.add_line("LIBRARY >> Unload event has been launched.")
    Draw.window.launch()
    log.add_line("LIBRARY >> The framework has been launched.")
    # create framework & thread & end_thread

if __name__ == "__main__":
    main()