def get_book_text(filepath):
    counted_words = 0
    with open(filepath) as file:
        data = file.read()
        words = data.split()
        counted_words += len(words)
    return counted_words


def counting_distinct_characters(filepath):
    f = open(filepath)
    counted_letters = []
    letter = {'letter':'a'}
    letter['count'] = f.read().upper().lower().count('a')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'b'}
    letter['count'] = f.read().upper().lower().count('b')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'c'}
    letter['count'] = f.read().upper().lower().count('c')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'d'}
    letter['count'] = f.read().upper().lower().count('d')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'e'}
    letter['count'] = f.read().upper().lower().count('e')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'f'}
    letter['count'] = f.read().upper().lower().count('f')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'g'}
    letter['count'] = f.read().upper().lower().count('g')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'h'}
    letter['count'] = f.read().upper().lower().count('h')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'i'}
    letter['count'] = f.read().upper().lower().count('i')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'j'}
    letter['count'] = f.read().upper().lower().count('j')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'k'}
    letter['count'] = f.read().upper().lower().count('k')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'l'}
    letter['count'] = f.read().upper().lower().count('l')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'m'}
    letter['count'] = f.read().upper().lower().count('m')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'n'}
    letter['count'] = f.read().upper().lower().count('n')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'o'}
    letter['count'] = f.read().upper().lower().count('o')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'p'}
    letter['count'] = f.read().upper().lower().count('p')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'q'}
    letter['count'] = f.read().upper().lower().count('q')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'r'}
    letter['count'] = f.read().upper().lower().count('r')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'s'}
    letter['count'] = f.read().upper().lower().count('s')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'t'}
    letter['count'] = f.read().upper().lower().count('t')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'u'}
    letter['count'] = f.read().upper().lower().count('u')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'v'}
    letter['count'] = f.read().upper().lower().count('v')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'w'}
    letter['count'] = f.read().upper().lower().count('w')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'x'}
    letter['count'] = f.read().upper().lower().count('x')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'y'}
    letter['count'] = f.read().upper().lower().count('y')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'z'}
    letter['count'] = f.read().upper().lower().count('z')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'æ'}
    letter['count'] = f.read().upper().lower().count('æ')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'â'}
    letter['count'] = f.read().upper().lower().count('â')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'ê'}
    letter['count'] = f.read().upper().lower().count('ê')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'ë'}
    letter['count'] = f.read().upper().lower().count('ë')
    counted_letters.append(letter)
    f.seek(0)
    letter = {'letter':'ô'}
    letter['count'] = f.read().upper().lower().count('ô')
    counted_letters.append(letter)

    sorted_letters_by_amount = sorted(counted_letters, reverse=True, key=lambda d: d['count'])
    i = 0
    for item in counted_letters:
        print(str(sorted_letters_by_amount[i]).replace("{","").replace("}","").replace("'letter'", "").replace("'count'", "").replace(":", "").replace(" ","").replace(",",": ").replace("'",""))
        i += 1
    return '============= END ==============='

