from stats import word_count

def read_file(path):
    with open (path) as f:
        return f.read()

def lower_case(text):
    return text.lower()

def char_count(text):
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def alpha_report(char_count):
    list = []
    for char in char_count:
        if char.isalpha():
            list.append({'character': char, 'count': char_count[char]})
    sorted_list = sorted(list, key=lambda x: x['character'])
    print("Generating report...")
    print("---------------------------------")
    for item in sorted_list:
        print(f"The character '{item['character']}' appears {item['count']} times.")

def main():
    text = read_file("books/frankenstein.txt")
    lower_text = lower_case(text)
    words = word_count(lower_text)
    chars = char_count(lower_text)
    # alpha_report(chars)
    print(f"Total words: {words}")
main()
