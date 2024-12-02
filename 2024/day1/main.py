# GOLD STAR #1
left_list = open('left.txt', 'r').read().splitlines()
right_list = open('right.txt', 'r').read().splitlines()

left_list.sort()
right_list.sort()

total_diff = 0

for index in range(len(left_list)):
  diff = abs(int(left_list[index]) - int(right_list[index]))
  total_diff += diff

print(total_diff)

# GOLD STAR #2
similarity = 0

for num in left_list:
  similarity += int(num) * right_list.count(num)

print(similarity)