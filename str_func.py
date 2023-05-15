def text_up(input_text):
"""функцию, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return input_text.upper

text_up(input_text)

def text_2up(input_text):
    """ функцию, которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции"""
    input_text = input_text[:2].upper()+input_text[2:]
    return input_text

text_2up(input_text)
