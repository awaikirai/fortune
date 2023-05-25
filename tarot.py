#!/usr/bin/env python3
# coding:UTF-8

def tarot():

    import random

    with open(".tarot_card") as card:
    
        all_data = card.read().splitlines()

    number = random.randint(0, 21)
    data = all_data[number].split(", ")
    position = random.randint(0, 1)

    return(
            "{0}:{1}の{2}\n"
            "概要:{3}\n"
            "意味:{4}".format(
                number, data[1], ("正位置", "逆位置")[position], data[2], data[3 + position]))

if __name__ == '__main__':
    print(tarot())

