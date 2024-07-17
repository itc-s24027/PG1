def make_func(pi = 3.14):
    # 円の面積を計算する関数を作る

    def ci_area(radius):
        # 円の面積を計算する

        return radius * radius * pi

    return ci_area

# piが初期設定(3.14)のとき
ci_area_default = make_func()
# piが3.1415926535のとき
ci_area_precise = make_func(pi = 3.1415926535)

print(ci_area_default(2))
print(ci_area_precise(2))
