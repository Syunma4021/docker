import os
import random

def janken():
    hands = {0 : "グー", 1 : "パー", 2 : "チョキ"}
    computerInt = random.randint(0, 2)

    print("じゃんけんを始めます")
    try:
        playerInt = int(input("いずれかの手を出してください（グー：0　パー：1　チョキ：2）："))
    except ValueError:
        print("無効な入力です")
        return
    else:
        if not 0 <= playerInt <= 2:
            print("無効な入力です")
            return

    if playerInt == computerInt:
        print("プレイヤー：" + hands[playerInt] + ", コンピューター：" + hands[playerInt])
        print("あいこです")
    elif (playerInt == 0 and computerInt == 2) or (playerInt == 1 and computerInt == 0) or (playerInt == 2 and computerInt == 1):
        print("プレイヤー：" + hands[playerInt] + ", コンピューター：" + hands[computerInt])
        print("プレイヤーの勝利です")
    else:
        print("プレイヤー：" + hands[playerInt] + ", コンピューター：" + hands[computerInt])
        print("プレイヤーの敗北です")

if __name__ == "__main__":
    janken()
