'''Write a python function to remove a given word from a list ad strip it at the same
time.'''

def remove_word(word, lst):
    if word in lst:
        lst.remove(word)        
    lst = [item.strip() for item in lst]
    return lst  
words = ['  apple', 'banana ', '  cherry', 'date  ']
word_to_remove = 'banana'       
updated_list = remove_word(word_to_remove, words)
print("Updated list:", updated_list)
    