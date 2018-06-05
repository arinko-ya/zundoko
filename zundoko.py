import random


def zundoko() -> None:
    zundoko_list = []
    for i in range(50):
        selected_string = random.choice(['ズン', 'ドコ'])
        print(selected_string)
        zundoko_list.append(selected_string)
        if 'ズンズンズンドコ' in ''.join(zundoko_list):
            print('キヨシ！！')
            zundoko_list.clear()


if __name__ == '__main__':
    zundoko()
