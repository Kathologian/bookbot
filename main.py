from stats import get_book_text
from stats import counting_distinct_characters

def main():
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {get_book_text('./books/frankenstein.txt')} total words')
    print('--------- Character Count -------')
    print(f'{counting_distinct_characters('./books/frankenstein.txt')}')
    #print('============= END ===============')

if __name__ == '__main__':
    main()