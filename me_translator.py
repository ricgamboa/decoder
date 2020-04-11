# Module used to translate the encrypted to clear text

from pathlib import Path

class Translator:

    def __init__(self, alphabet_size):
        self.alph_size = alphabet_size
        self.alphabet = []

    def set_alphabet(self, alph_file):
        # read the alphabet
        alph_path = Path.cwd().joinpath("project_files", alph_file)
        alph = []
        with open(alph_path, "rt") as alph_str:
            for line in alph_str:
                alph.append(line.strip()[-7:].split(","))
        self.alphabet = alph

    def translate(self, encryp_answer, alph_index_list):
        # translate the answer with the known alphabets
        plain_answer = []
        count = 0
        for letter in encryp_answer:
            alph_index = alph_index_list[count]
            plain_answer.append(self.alphabet[alph_index].index(letter))
            count += 1
        return plain_answer
