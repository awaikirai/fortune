#!/usr/bin/env python3
# coding:UTF-8

def toss():

    import random

    coin = random.randint(0, 1)

    return(coin)


if __name__ == '__main__':

    print(("裏", "表")[toss()])

