def analyze_string(s):
    vowels = "aeiouAEIOU"
    vowels_in_str = ""
    consonants_in_str = ""
    consonant_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowels_in_str += char
            else:
                consonants_in_str += char
                consonant_count += 1

    result = (vowels_in_str, consonant_count, consonants_in_str)
    return result

# приклад використання
input_string = "abcdefg"
output = analyze_string(input_string)
print(output)
