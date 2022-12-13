from src.libraries import *

### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa

class log:

    log_path = os.getcwd() + "\\config\\log.txt"
    log = {}

    def __init__(self):
        if not os.path.isdir(os.getcwd() + "\\config"):
            os.mkdir(os.getcwd() + "\\config")
        f = open(self.log_path, "w+")
        f.write("LOG BEGIN\n")
        f.close()

    def add_line(self, string):
        f = open(self.log_path, "a")
        f.write(string + "\n")
        f.close()