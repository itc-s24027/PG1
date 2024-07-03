# typeを使ってデータの型を調べる
print(type(3))
print(type(3.1))
a = 3
print(type(a))

# データが整数型か確認する
print(type(a) is int)
print(type(a) is float)

#データ型を調べる組み込み関数
print(isinstance(a,int))

# べき乗
print(pow(2,10))
print(pow(16,0.5))
print(pow(9,22,23))
print(divmod(13,5))

# 少数を整数に丸める
print(round(2.672,2))
print(round(2.679,2))
print(round(1.5))
print(round(2.5))
print(round(2.675,2))
