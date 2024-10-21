def single_root_words(root_word: str, *other_words):
   same_word = []
   for word in other_words:
      if root_word.lower() in word.lower() or word.lower() in root_word.lower():
         same_word.append(word)
   return same_word

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)