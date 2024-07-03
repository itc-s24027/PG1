# ユーザーから入力を受け取る
name = input('お名前は?')
print(name)

# 文字列やリストの長さをlen関数で調べる
print(len(name))

#
name_iter = iter(name)
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))

