# 使用字典dict统计

lists = ["a", "b", "c", 1, 2, 3, 1]
count_dist = dict()
for i in lists:
    if i in count_dist:
        count_dist[i] += 1
    else:
        count_dist[i] = 1
print(count_dist)

