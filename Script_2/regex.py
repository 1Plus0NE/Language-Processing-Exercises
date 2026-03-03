import re

texto = """A 03/01/2022, V foi de férias com a sua família.
Ficaram hospedados num hotel e aproveitaram as férias para passear e descobrir novos locais.
Mais tarde, no dia 12/01/2022, V voltou para casa e começou a trabalhar num novo projeto.
Passou muitas horas no computador, mas finalmente terminou o projeto a 15/01/2022.
Alguns meses depois, a 26/09/2023, V casou-se com Judy e no dia 30/09/2023 partiram na
sua lua-de-mel para o local onde V tinha ido de férias no ano anterior."""

texto2 = """Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA].
Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo.
Talvez os [NOME PLURAL MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""

um = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "MEI": "Mestrado em Engenharia Informática",
    "LCC": "Licenciatura em Ciências da Computação",
    "CG": "Campus de Gualtar",
    "EG": "Engenharia Gramatical",
    "DI": "Departamento de Informática",
    "EEUM": "Escola de Engenharia da Universidade do Minho"
}

expanse = {
    "UNN": "United Nations Navy",
    "OPA": "Outer Planets Alliance",
    "MCRN": "Martian Congressional Republic Navy",
    "PDC": "Point Defense Cannon",
    "PB": "Protomolecule-Based"
}

internet = {
    "tbh": "to be honest",
    "idk": "I don't know",
    "afaik": "as far as I know",
    "imo": "in my opinion",
    "nbd": "no big deal"
}

def iso_date(text):

    regex = r'\d{4}-\d{2}-\d{2}'
    return re.fullmatch(regex, text) != None

def float_num(text):

    regex = r'(([+-]?\d+\.\d+)|([+-]?\.\d+))(([eE][+-]?)\d+)?'
    return re.fullmatch(regex, text) != None

def email(text):

    regex = r'\w+(\.\w+)*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+'
    return re.fullmatch(regex, text) != None

def proper(text):
    """
     Retrieves all proper nouns from a text. A proper noun is any sequence of words
     that starts with an upper-case letter, except if it is in the beginning of a
     sentence.
    """

    regex = r'(?<!^)[A-Z][a-zA-Z]*(?:\s+[A-Z][a-zA-Z]*)*' # (?<!^) is used to ignore the first character/string that shows up
    return re.findall(regex, text)

def sum_uints(text):
    """
     Sums all occurrences of unsigned integers numbers in a text.
    """
    regex = r'\b\d+\b'
    return sum(map(int, re.findall(regex, text)))

def sum_ints(text):
    """
     Sums all occurrences of possibly unsigned integers numbers in a text.
    """
    regex = r'\b[+-]?\d+\b'
    return sum(int(x) for x in re.findall(regex, text))

def euros(text):
    """
     Retrieves all occurrences of euro € quantities from a text.
    """
    regex = r'€\s*(\d+(\.\d+)?)|(\d+(\.\d+)?)\s*€'
    matches = re.finditer(regex, text)
    
    result = []
    for m in matches:
        result.append(m.group(0))  # match completo
    
    return result

def iso_8601(text):
    """
     Convert dates written in DD/MM/AAAA format to the ISO 8601 format AAAA-MM-DD.
    """
    regex = r'(\d{2})/(\d{2})/(\d{4})'

    return re.sub(regex, r'\1-\2-\3', text)

def expand(text, dct):
    regex = r'/acronym\{([A-Z]+)\}'

    def expand_sub(match):
        key = match.group(1) # grupo que representa a string entre {}
        return dct.get(key, key) # mantém o valor anterior se não houver match sobre a key

    return re.sub(regex, expand_sub, text)

def mad_libs():

    regex = r'\[(.+?)\]'

    return re.sub(regex, lambda m: input(f"Give me a ({m.group(1)}): "), texto2)

def rem_repeated(text):
    regex = r'(\w+)(s+)(\1\s+)*'

    return re.sub(regex, r'\1\2', text, flags=re.I)

def main():

    print(rem_repeated("It was very very VERY hot."))

if __name__ == "__main__":
    main()