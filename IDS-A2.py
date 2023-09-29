import re

def removePunct(text):
  words=re.sub(r'[^\w\s]','',text)
  return words

def replaceN(text):
  text = re.sub(r'\b(\w+)n\'t\b', r'\1 not', text)
  return text

def replaceS(text):
  text = re.sub(r'\n+', ' ', text)
  return text

def main():
  with open('example-text.txt', 'r') as f:
    text = f.read()

  words = re.findall(r'\w+',text)
  print('List of all words:',words)
  print()
  print()

  capt=re.findall(r'[A-Z]\w+',text)
  print('List of all words starting with a capital letter:',capt)
  print()
  print()

  words5 = re.findall(r'\w{5}',text)
  print('List of all words of length 5:',words5)
  print()
  print()

  double_quotes = re.findall(r'"(.*?)"', text)
  print('List of all words inside double quotes:', double_quotes)
  print()
  print()

  vowels = re.findall(r'[aeiou]',text)
  print('List of all vowels:', vowels)
  print()
  print()

  E3 = re.findall(r'\w{2}e',text)
  print('List of 3 letter words ending with letter:',E3)
  print()
  print()

  Bwords = re.findall(r'^b\w+b$',text)
  print('List of all words starting and ending with letter ‘b’:',Bwords)
  print()
  print()

  Punct = removePunct(text)
  print('Removed all the punctuation marks from the text:')
  print(Punct)
  print()
  print()

  Not = replaceN(text)
  print('Replaced all words ending nt to their full form not:')
  print(Not)
  print()
  print()

  space = replaceS(text)
  print('Replaced all the new lines with a single space:')
  print(space)
  print()
  print()

main()
