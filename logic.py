# Задание №3
import requests
from collections import defaultdict
from translate import Translator
# Задание №5
qwestions={"what is your name":"im super-bot and i was created to help you!","how old are you":"its is philosophical question"}

class TextAnalysis():   
    
    # Задание №1
    memory=defaultdict(list)
    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        if self.text in qwestions.keys():
            self.response = self.get_answer()
        else:
            self.response = self.get_answer()
    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang,to_lang=to_lang)
            translation = translator.translate(text)
            return translator
            # Задание №4
        except:
            return "Перевод не удался"

    def __deep_pavlov_answer(self):
        try:
            API_URL = "https://7038.deeppalov.ai/model"
            data={"quastion_raw": [ self_translation ]}
            res = requests.post(API_URL, json=data).json()
            res = res[0][0]
        except:
            res=('i dont know how to help you ')
        return res
