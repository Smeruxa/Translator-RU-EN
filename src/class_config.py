from src.libraries import *

### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa

class config:

    global GetSystemMetrics

    config_path = os.getcwd() + "\\config"
    screen_x, screen_y = GetSystemMetrics(0), GetSystemMetrics(1)
    default_config = {
        "x": str(int(screen_x / 2 - 400)),
        "y": str(int(screen_y / 2 - 77)),
        "speak": "Русский"
    }
    config = {}

    def __init__(self):
        if not os.path.isdir(self.config_path) or not os.path.isfile(self.config_path + "\\config.ini"):
            if not os.path.isdir(self.config_path):
                os.mkdir(self.config_path)
            f = open(self.config_path + "\\config.ini", "w+")
            for key, item in self.default_config.items():
                f.write(key + "=" + item + "\n")
                self.config[key] = item
            f.close()
        else:
            f = open(self.config_path + "\\config.ini", "r")
            for i, line in enumerate(f):
                values = re.match(r"(.+)=(.+)", line)
                if values:
                    self.config[values[1]] = values[2]
            f.close()

    def get(self):
        return self.config 
    
    def save(self, table):
        if os.path.isfile(self.config_path + "\\config.ini"):
            f = open(self.config_path + "\\config.ini", "w+")
            for key, item in self.default_config.items():
                f.write(key + "=" + table[key] + "\n")
            f.close()
        else:
            print("Error >> File Dont Exist")