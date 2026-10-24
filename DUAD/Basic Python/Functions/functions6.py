#6
# 6. Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
#words_order = "python-variable-funcion-computadora-yoyo-monitor"
words_order = "abeja-python-zorro-monitor"
#v1 duplicates dont work
def re_convert_string(word_list):
    string_new = ""
    # for word in word_list: #v1
    #     string_new += word #v1
    #     if word_list.index(word) < len(word_list) - 1: #v1
    #        string_new += "-"
    for i in range(len(word_list)): #v2
        string_new += word_list[i] #v2
        if i < len(word_list) - 1: #v2
            string_new += "-"
    return string_new

def order_string(string):
    list_of_words = str(string).split("-")
    temporary_list = []
    flag_index = -1
    flag_order = ""
    for word in list_of_words:
        if len(temporary_list) == 0:
            temporary_list.append(word)
            continue
        for i in range(len(temporary_list)):
            word2 = temporary_list[i]
            if word > word2 and (flag_order == "" or flag_order == "MAYOR"):
                flag_index = i + 1
                flag_order = "MAYOR"
            elif word < word2 and (flag_order == "" or flag_order == "MENOR"):
                flag_index = i
                flag_order = "MENOR"
                break
            elif word == word2:
                flag_index = i
                break
        if flag_index != -1:
            temporary_list.insert(flag_index,word)
            flag_index = -1
            flag_order = ""   
    return re_convert_string(temporary_list)
#6


if __name__ == '__main__':
    print(f"The original word list is {words_order} and it has been ordered {order_string(words_order)} with type {type(order_string(words_order))}")