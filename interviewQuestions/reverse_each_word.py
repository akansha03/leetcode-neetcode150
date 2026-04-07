'''
6️⃣ Reverse Each Word in a Sentence:
Given "abc de f", reverse each word individually while keeping spaces in place. The expected output is "cba ed f.
'''
def reverse(s):
    t = ''
    for i in range(len(s)-1, -1, -1):
        t += s[i]
    return t

def reverse_each_word(s):
    temp = s.split(" ")
    result = []
    for t in temp:
        result.append(reverse(t))
    return ' '.join(result)

def two_pointer_approach(s):
    left = right = 0
    n = len(s)
    result = []
    while left <= right < n:
        while right<n and s[right] != ' ':
            right += 1
        result.append(reverse(s[left:right]))
        right += 1
        left = right
    return ' '.join(result)

word = "abc de f"
print(f'Reverse using split: {reverse_each_word(word)}')
print(f'Reverse using two pointer approach : {two_pointer_approach(word)}')