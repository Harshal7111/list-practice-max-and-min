score_list = []
len_list = int(input("Enter length of the list: "))

for i in range(len_list):
  num = int(input("Enter a number: "))
  score_list.append(num)
print(score_list)

max_num = score_list[0]
for j in range(len_list-1):
  if max_num > score_list[j+1]:
    print()
  else:
    max_num = score_list[j+1]
print(f"{max_num} is the greatest number in the list.")

min_num  = score_list[0]
for n in range(len_list-1):
  if min_num < score_list[n+1]:
    print()
  else:
    min_num = score_list[n+1]
print(min_num)

  