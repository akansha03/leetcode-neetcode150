'''
7️⃣ Find anagram which is a substring. Input 1 = "programming", Input 2 = "gram". Output: true.
Input 3 = "Hello"
Input 4 = "World"
Output: false
'''

def word_anagram(word_1, word_2):

    if len(word_1) != len(word_2):
        return False

    freq = [0]*26
    for w in word_1.lower():
        freq[ord(w) - ord('a')] += 1
    for w in word_2.lower():
        freq[ord(w) - ord('a')] -= 1

    return all(f==0 for f in freq)

print(word_anagram("Hello", "World"))
