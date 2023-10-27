# Same as the words in phone number but created without explicitly defining the letter_to_number.
# The question is.  Imagine as old style phone pad on your mobile where letters are assigned to numbers.  
# Create a function that given a phone number and a list of words show how many words are in the phone number. 
# The words must be in a continuous sequence. 

# Function to convert a word to its numeric representation
def word_to_number(word):
    numeric_representation = ''
    for char in word:
        char = char.lower()  # Convert to lowercase to handle uppercase letters
        if 'a' <= char <= 'c':
            numeric_representation += '2'
        elif 'd' <= char <= 'f':
            numeric_representation += '3'
        elif 'g' <= char <= 'i':
            numeric_representation += '4'
        elif 'j' <= char <= 'l':
            numeric_representation += '5'
        elif 'm' <= char <= 'o':
            numeric_representation += '6'
        elif 'p' <= char <= 's':
            numeric_representation += '7'
        elif 't' <= char <= 'v':
            numeric_representation += '8'
        elif 'w' <= char <= 'z':
            numeric_representation += '9'
    return numeric_representation

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
phone_number = "2276696"  # Example phone number
word_list = ["cap", "foo", "bar", "baz"]  # Example list of words

result = count_continuous_words_in_phone_number(phone_number, word_list)
print(f"Number of words found in {phone_number} in a continuous sequence: {result}")
