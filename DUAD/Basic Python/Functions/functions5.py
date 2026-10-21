#5
# 5. Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
count_me_word = "I love Nación Sushi"
def upper_and_lower_count(count_word):
    lower_count = 0
    upper_count = 0
    for letter in count_word:
        if letter.islower():
            lower_count += 1
        elif letter.isupper(): #Spaces mess this count so else not valid
            upper_count += 1
    return f"{upper_count} upper characters and {lower_count} lower characters"
#5

if __name__ == '__main__':
    print(f"The word is {count_me_word} and it has {upper_and_lower_count(count_me_word)}")