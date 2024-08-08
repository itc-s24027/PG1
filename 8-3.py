import collections

data = 'すもももももももものうち'
count_dic = {}
for v in data:
    if v in count_dic:
        count_dic[v] += 1
    else:
        count_dic[v] = 1
print(count_dic)

count_dic = collections.defaultdict(int)
for v in data:
    count_dic[v] += 1
print(count_dic)

count_dic = collections.defaultdict(list)
for v in data:
    count_dic[v].append(v)
print(count_dic)

counter = collections.Counter(data)
print(counter)

print(counter['す'])
print(counter['ぽ'])
print(counter['も'])

print(counter.most_common())
print(counter.most_common(2))

CharCount = collections.namedtuple('CharCount', ['char', 'count'])
mo = CharCount('も', 8)
print(mo)
print(mo.char, mo.count)

count = collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch, cnt in count.items():
    res_dict[cnt].append(ch)
print(res_dict[1])
