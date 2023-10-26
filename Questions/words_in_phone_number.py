#image an old style phone that has letters assigned to numbers.  
#Find how many words appear in a phone number.

# Define the mapping of letters to numbers
letter_to_number = {
    'a': '2', 'b': '2', 'c': '2',
    'd': '3', 'e': '3', 'f': '3',
    'g': '4', 'h': '4', 'i': '4',
    'j': '5', 'k': '5', 'l': '5',
    'm': '6', 'n': '6', 'o': '6',
    'p': '7', 'q': '7', 'r': '7', 's': '7',
    't': '8', 'u': '8', 'v': '8',
    'w': '9', 'x': '9', 'y': '9', 'z': '9'
}
# Function to convert a word to its numeric representation
def word_to_number(word):
    return ''.join(letter_to_number.get(c, '') for c in word)

# Function to count how many words from the list can be formed from the phone number
def count_continuous_words_in_phone_number(phone_number, word_list):
    phone_number = str(phone_number)
    phone_number_length = len(phone_number)
    count = 0

    for word in word_list:
        word_numeric = word_to_number(word)
        word_length = len(word_numeric)

        for i in range(phone_number_length - word_length + 1):
            substring = phone_number[i:i + word_length]

            if word_numeric == substring:
                count += 1
                break  # Break if a match is found to avoid double counting

    return count

# Example usage
phone_number = "22276696366"  # Example phone number
word_list = ["cap", "foo", "bar", "baz", "abc"]  # Example list of words

result = count_continuous_words_in_phone_number(phone_number, word_list)
print(f"Number of words found in {phone_number} in a continuous sequence: {result}")
