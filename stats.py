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


"""
def counting_distinct_characters(filepath):
    f = open(filepath)
    letters = []
    letters.append({'a':f.read().upper().lower().count('a')}) 
    f.seek(0)
    letters.append({'b':f.read().upper().lower().count('b')})

    #letters_sorted = dict(sorted(letters.items(), key=lambda item: item[1]))  

    i = 0
    for item in letters:
        print(str(letters[i]).replace("{","").replace("}",""))
        i += 1
    return '============= END ==============='
"""

"""
def counting_distinct_characters(filepath):
    counted_letters = []
    
    with open(filepath) as f:
        letter = {'letter':'a'}
        letter['count'] = f.read().upper().lower().count('a')
        counted_letters.append(letter)
    with open(filepath) as f:
        letter = {'letter':'b'}
        letter['count'] = f.read().upper().lower().count('b')
        counted_letters.append(letter)

    #print('\n'.join("{}: {}".format(k, v) for k, v in counted_words.items()))
    #print(f'{count_a['letter']}: {count_a['count']}\n')
    print(f'{counted_letters}') #.sort(reverse=True, key=letter)
    return '============= END ==============='
"""
"""
    with open(filepath) as f:
        count_b = f.read().upper().lower().count('b')
        counted_words.append(count_b)
    with open(filepath) as f:
        count_c = f.read().upper().lower().count('c')
        counted_words.append(count_c)
    with open(filepath) as f:
        count_d = f.read().upper().lower().count('d')
        counted_words.append(count_d)
    with open(filepath) as f:
        count_e = f.read().upper().lower().count('e')
        counted_words.append(count_e)
    with open(filepath) as f:
        count_f = f.read().upper().lower().count('f')
        counted_words.append(count_f)
    with open(filepath) as f:
        count_g = f.read().upper().lower().count('g')
        counted_words.append(count_g)
    with open(filepath) as f:
        count_h = f.read().upper().lower().count('h')
        counted_words.append(count_h)
    with open(filepath) as f:
        count_i = f.read().upper().lower().count('i')
        counted_words.append(count_i)
    with open(filepath) as f:
        count_j = f.read().upper().lower().count('j')
        counted_words.append(count_j)
    with open(filepath) as f:
        count_k = f.read().upper().lower().count('k')
        counted_words.append(count_k)
    with open(filepath) as f:
        count_l = f.read().upper().lower().count('l')
        counted_words.append(count_l)
    with open(filepath) as f:
        count_m = f.read().upper().lower().count('m')
        counted_words.append(count_m)
    with open(filepath) as f:
        count_n = f.read().upper().lower().count('n')
        counted_words.append(count_n)
    with open(filepath) as f:
        count_o = f.read().upper().lower().count('o')
        counted_words.append(count_o)
    with open(filepath) as f:
        count_p = f.read().upper().lower().count('p')
        counted_words.append(count_p)
    with open(filepath) as f:
        count_q = f.read().upper().lower().count('q')
        counted_words.append(count_q)
    with open(filepath) as f:
        count_r = f.read().upper().lower().count('r')
        counted_words.append(count_r)
    with open(filepath) as f:
        count_s = f.read().upper().lower().count('s')
        counted_words.append(count_s)
    with open(filepath) as f:
        count_t = f.read().upper().lower().count('t')
        counted_words.append(count_t)
    with open(filepath) as f:
        count_u = f.read().upper().lower().count('u')
        counted_words.append(count_u)
    with open(filepath) as f:
        count_v = f.read().upper().lower().count('v')
        counted_words.append(count_v)
    with open(filepath) as f:
        count_w = f.read().upper().lower().count('w')
        counted_words.append(count_w)
    with open(filepath) as f:
        count_x = f.read().upper().lower().count('x')
        counted_words.append(count_x)
    with open(filepath) as f:
        count_y = f.read().upper().lower().count('y')
        counted_words.append(count_y)
    with open(filepath) as f:
        count_z = f.read().upper().lower().count('z')
        counted_words.append(count_z)
    with open(filepath) as f:
        count_æ = f.read().upper().lower().count('æ')
        counted_words.append(count_æ)
    with open(filepath) as f:
        count_â = f.read().upper().lower().count('â')
        counted_words.append(count_â)
    with open(filepath) as f:
        count_ê = f.read().upper().lower().count('ê')
        counted_words.append(count_ê)
    with open(filepath) as f:
        count_ë = f.read().upper().lower().count('ë')
        counted_words.append(count_ë)
    with open(filepath) as f:
        count_ô = f.read().upper().lower().count('ô')
        counted_words.append(count_ô)

    counted_words.sort(reverse=True)
    print(f'a: {counted_words[0]}\nb: {counted_words[1]}\nc: {counted_words[2]}\nd: {counted_words[3]}\ne: {counted_words[4]}\nf: {counted_words[5]}')
    print(f'g: {counted_words[6]}\nh: {counted_words[7]}\ni: {counted_words[8]}\nj: {counted_words[9]}\nk: {counted_words[10]}\nl: {counted_words[11]}')
    print(f'm: {counted_words[12]}\nn: {counted_words[13]}\no: {counted_words[14]}\np: {counted_words[15]}\nq: {counted_words[16]}\nr: {counted_words[17]}')
    print(f's: {counted_words[18]}\nt: {counted_words[19]}\nu: {counted_words[20]}\nv: {counted_words[21]}\nw: {counted_words[22]}\nx: {counted_words[23]}')
    print(f'y: {counted_words[24]}\nz: {counted_words[25]}\næ: {counted_words[26]}\nâ: {counted_words[27]}\nê: {counted_words[28]}\në: {counted_words[29]}')
    print(f'ô: {counted_words[30]}')
    return '============= END ==============='
    """
