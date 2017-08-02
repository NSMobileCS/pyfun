# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']



def find_words_with_char(char, arr):
    return [word for word in arr if char in word]

print(find_words_with_char('x', ['the', 'very', 'xtreme', 'zebra', 'exrayed', 'the', 'article']))