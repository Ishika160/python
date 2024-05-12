def get_unique_words(file_path):
    unique_words = set()  # Use a set to store unique words
    
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into words and add them to the set
            words = line.split()
            unique_words.update(words)
    
    return unique_words

# Example usage:
file_path = input("Enter the path to the text file: ")

try:
    unique_words = get_unique_words(file_path)
    print("Unique words in the file:")
    for word in unique_words:
        print(word)
except FileNotFoundError:
    print("File not found. Please enter a valid file path.")
