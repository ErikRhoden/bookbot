def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = total_words(text)
    
    print("Please enter a word to see how many times it was mentioned in the story.")
    mentioned = input("")
    num_times = word_mentioned(mentioned, text)

    print("==========================================")
    print(f"\n--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    print(f"'{mentioned}' was mentioned a total of {num_times} times\n")

    dict = count_letters(text)
    letters = [{'char': key, 'num': value} for key, value in dict.items()]
    letters.sort(reverse=True, key=sort_on)
    
    for letter in letters:
        print(f"The '{letter['char']} character was found {letter['num']} times")
    
    print("--- End report ---")
    print("==========================================")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_mentioned(mentioned, text):
    count = 0
    lower_text = text.lower()
    words = lower_text.split()
    lower_mentioned = mentioned.lower()
    for word in words:
        if lower_mentioned == word:
            count += 1
    return count

def total_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_letters(text):
    letters = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter not in letters and letter.isalpha():
            letters[letter] = 1
        elif letter in letters and letter.isalpha():
            letters[letter] += 1
    return letters

def sort_on(dict):
    return dict["num"]

main()
