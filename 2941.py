word = input()
Cword = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in Cword:
  word = word.replace(i, '*')

print(len(word))
