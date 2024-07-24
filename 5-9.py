mountain_in_japan = {'fuji': 3776, 'kitadake': 3193, 'okuhodakadake': 3190}
print('● 山名順にソート')
mountain_in_japan_sorted = sorted(mountain_in_japan.items(), key=lambda x: x[0])
for key, val in mountain_in_japan_sorted:
    print(key, val)
print('● 標高順にソート')
mountain_in_japan_sorted = sorted(mountain_in_japan.items(), key=lambda x: x[1])
for key, val in mountain_in_japan_sorted:
    print(key, val)
print('● 標高の逆順にソート')
for key, val in reversed(mountain_in_japan_sorted):
    print(key, val)
