def counting_words_in_book(filepath):
  count = 0
  with open(filepath, 'r') as f:
    data = f.read()
    words = data.split()
    count += len(words)
  return count

def counting_distinct_characters(filepath):
    with open(filepath) as f:
        count_t = f.read().upper().lower().count('t')
    with open(filepath) as f:
        count_p = f.read().upper().lower().count('p')
    with open(filepath) as f:
        count_c = f.read().upper().lower().count('c')
        characters = {'t':count_t, 'p':count_p, 'c':count_c}
    return characters       

"""
def counting_distinct_characters(filepath):
    with open(filepath) as f:
        count_t = f.read().upper().lower().count('t')
        count_p = f.read().upper().lower().count('p')
        count_c = f.read().upper().lower().count('c')
        characters = {'t':count_t, 'p':count_p, 'c':count_c}
        return characters       
"""        