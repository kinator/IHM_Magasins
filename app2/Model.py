import json

class Model:
    def __init__(self):
        self.data = {}

    def load_data(self, filepath):
        try:
            with open(filepath, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Fichier {filepath} introuvable.")

    def get_data(self):
        return self.data
