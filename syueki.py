#!/usr/bin/env python3
# coding:UTF-8

#1, 内容を決める

#2, ５０本の筮竹から１本抜き取る（太極）

#3, 両手の左右２つの束に分ける（天策：地策）

#4, 地策（右）を置き、そこから１本抜き取って左手の小指と薬指の間にはさむ（人策）

#5, 天策（左）を４本ずつ抜き取り続け、余った策（割り切れる場合は４とする）を薬指と中指の間にはさむ

#6, 地策を４本ずつ抜き取り続け、余った策（０を含む）を中指と人差し指の間にはさむ

#7, はさんだ策数を合計すると５か９になる（第一変）

#8, はさんだ策を除いて３～６を繰り返すと合計が４か８になり、さらに繰り返しても４か８になる（第二変、第三変）

#9, 第一変から第三変までの左手にはさんだ策を足して４９から引くと２４，２８，３２，３６（４の６倍、７倍、８倍、９倍）となる

#10, ６は老陰、７は少陽、８は少陰、９は老陽とし、６，８を陰、７，９を陽とする（初爻）

#11, これを合計６回繰り返し、下から陰陽を決めて六爻を定める

def hen(zeitiku):
    import random
    
    tentiku = random.randrange(1, zeitiku)
    titiku = zeitiku - tentiku
    
    zintiku = 1
    titiku -= zintiku

    while tentiku > 4:
        tentiku -= 4

    while titiku > 4:
        titiku -= 4

    return(tentiku + zintiku + titiku)

def kou(zeitiku):
    iti = hen(zeitiku)
    ni = hen(zeitiku - iti)
    san = hen(zeitiku - iti - ni)

    return((zeitiku - (iti + ni + san)) / 4)

def syueki(zeitiku):
    roku = {}
    for k in range(1, 7):
        roku[k] = kou(zeitiku)

    return(roku)


if __name__ == '__main__':
    
    rokkou = syueki(50-1)
    for i in range(len(rokkou), 0, -1):
        if rokkou[i] % 2 == 1:
            print("---")
        else:
            print("- -")


