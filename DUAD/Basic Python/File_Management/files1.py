# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

with open("songs.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

temporary_list = []

for line in lines:
    word = line.strip()
    flag_index = -1
    flag_order = ""

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
        temporary_list.insert(flag_index, word)
    else:
        temporary_list.append(word)

with open("songs_sorted.txt", 'w', encoding='utf-8') as file:
    for song in temporary_list:
        file.write(song + "\n")
