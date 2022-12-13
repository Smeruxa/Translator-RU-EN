from src.libraries import *

### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa
### AUTHOR -->> vk.com/wfsmeruxa | Smeruxa

class translate:

    def __init__(self):
        self.main_translator = Translator()

    def translate(self, text, t_from="ru", t_to="en"):
        result = self.main_translator.translate(text, src=t_from, dest=t_to)
        return result.text 