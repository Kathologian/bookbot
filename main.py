from stats import counting_words_in_book
from stats import counting_distinct_characters

"""def get_book_text(filepath):
  with open(filepath) as f:
    contents = f.read()
    return contents"""


def main():
  print(f"Found {counting_words_in_book("./books/frankenstein.txt")} total words")
  print(f"{counting_distinct_characters("./books/frankenstein.txt")}")
  #print(f"{get_book_text("./books/frankenstein.txt")}")

if __name__== "__main__":
  main()


"""
def number_of_words(contents): # this should take the result of def get_book_text and count the words to return the word count
  word_count = 0
  contents = contents.get_book_text()
  contents.split()
  for word in contents:
    word_count += 1
  return word_count


def main(): #The main function that calls on the get_book_text and number_of_word functions
  word_count = word_count.number_of_words
  filepath = "./books/frankenstein.txt"
  get_book_text(filepath)
  print(f"{word_count} words found in the document")


main()

# This works 

def get_book_text(filepath):
  with open(filepath) as f:
    contents = f.read()
  print(contents)

def main():
  filepath = "./books/frankenstein.txt"
  get_book_text(filepath)

main()
-----------------------------------------
def get_book_text(filepath):
  with open(filepath) as f:
    contents = f.read()
  print(contents)

def main():
  print(f"{get_book_text("./books/frankenstein.txt")}")

if __name__=="__main__":
  main()
  
"""
  