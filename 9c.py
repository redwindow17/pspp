def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
file_name=input("Enter the file name:")
print(longest_word (file_name))
