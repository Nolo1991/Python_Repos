
def alternate_word_case(text):
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return " ".join(result)

input_text = "Nolonwabo is learning Python"

print(input_text)
print(f"{alternate_word_case(input_text)}")