def perrin(m=100):
    '''mより小さなペラン数列をリストで返す

    ペラン数列:3,0,2,3,3,5,5,7,10,12,17,22,29,39,...
    '''
    a,b,c = 3,0,2
    result = []
    while a < m:
        result.append(a)
        a,b,c = b,c,a+b
    return result

# 間違えて問題２を書いてしまいました
