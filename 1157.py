word = input().upper()
word_list = list(set(word)) #set함수 사용해서 중복된 문자값 제거
cnt = []

for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print('?')
else:
  print(word_list[(cnt.index(max(cnt)))])