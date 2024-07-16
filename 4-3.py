def show_args(*args):
    '''与えられた複数の位置引数をタプルにまとめて受取そのタプルを表示して返す'''
    print('Positional arguments:', args)
    return args

def show_kwargs(**kwargs):
    '''与えられたキーワード引数を辞書にまとめて受取その辞書を表示して返す'''
    print('Keyword arguments:', kwargs)
    return kwargs
