import json, copy, os, sys
import cadrillage

class Fichier(object):

    def __init__(self, jsonFile : (str|None) = None) -> None:
    
        # attributs
        self.__current : (int|None) = None
        
        # si un fichier est fourni : on charge
        if jsonFile:
            self.open(jsonFile)


    @property
    def current(self) -> int | None :
        return self.__current
    

    @current.setter
    def current(self, index :int|None) -> None :
        self.__current = index

    def open(self, jsonFile : str):
        with open(jsonFile, encoding='utf-8') as file:
        
            print(f'loading file: {jsonFile}', end='... ')
            js = json.load(file)
        
            if 'cases' in js.keys():
        
                cases = js['cases']
        
                # for p in cases:
                #     #pp = cases..buildFromJSon(p)
                #     self.__cases.append(pp)
        
                self.__current = 0 if self.__cases else None

    def save(self, jsonFile : str) -> None:
        print(f'saving file: {jsonFile}', end='... ')

        if not os.path.exists(jsonFile):
            f = open(jsonFile, "x")
            f.close()

        with open(jsonFile, "w", encoding='utf-8') as file:

            d : dict= {}
            cases : list= []
            
            for p in self.__cases :
                cases.append(json.loads(p.toJSON()))
            
            d['annuaire'] = cases
            json.dump(d,file,ensure_ascii=False)
        
        print(f'done!')