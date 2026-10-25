# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_songs(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    songs = []

    for line in lines:
        song = line.strip()
        songs.append(song)

    return songs


def sort_songs(songs):
    temporary_list = []

    for word in songs:
        flag_index = -1
        flag_order = ""

        if len(temporary_list) == 0:
            temporary_list.append(word)
            continue

        for i in range(len(temporary_list)):
            word2 = temporary_list[i]

            if word > word2 and (
                flag_order == "" or flag_order == "GREATER"
            ):
                flag_index = i + 1
                flag_order = "GREATER"

            elif word < word2 and (
                flag_order == "" or flag_order == "LESSER"
            ):
                flag_index = i
                flag_order = "LESSER"
                break

            elif word == word2:
                flag_index = i
                break

        if flag_index != -1:
            temporary_list.insert(flag_index, word)
        else:
            temporary_list.append(word)

    return temporary_list


def write_songs(filename, songs):
    with open(filename, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song + "\n")


def main():
    songs = read_songs("songs.txt")
    sorted_songs = sort_songs(songs)
    write_songs("songs_sorted.txt", sorted_songs)


if __name__ == "__main__":
    main()