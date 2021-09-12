import os


def check_or_make_fir(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    check_or_make_fir('dataset/model')
