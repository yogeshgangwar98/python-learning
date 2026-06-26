from constants import BASE_URL
from collections import Counter

def frequent_word(filename):
    with open(filename,"r") as file:
        content = file.read()
        words = [word.replace('.', '').lower() for word in content.split()]
        return Counter(words).most_common(1)[0]

print(frequent_word(BASE_URL+"most_freq.txt"))