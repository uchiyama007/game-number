import random

def main():
    print("数字推測ゲームへようこそ！")

    # ユーザーから最小値と最大値を取得
    while True:
        try:
            n = int(input("最小値を入力してください: "))
            m = int(input("最大値を入力してください: "))
            if n <= m:
                break
            else:
                print("エラー: 最小値は最大値以下でなければなりません。")
        except ValueError:
            print("エラー: 有効な整数を入力してください。")

    # 指定された範囲内で乱数を生成
    secret_number = random.randint(n, m)
    max_attempts = 5  # 最大試行回数
    attempts = 0

    print(f"{n} から {m} の範囲内で数字を推測してください。最大 {max_attempts} 回の試行が可能です。")

    # ゲームループ
    while attempts < max_attempts:
        try:
            guess = int(input("あなたの推測: "))
            attempts += 1
            
            if guess < n or guess > m:
                print(f"推測は {n} から {m} の範囲内でなければなりません。")
                continue
            
            if guess < secret_number:
                print("もっと大きい数字です。")
            elif guess > secret_number:
                print("もっと小さい数字です。")
            else:
                print(f"おめでとうございます！正解は {secret_number} でした。")
                break

        except ValueError:
            print("エラー: 有効な整数を入力してください。")

    if attempts == max_attempts:
        print(f"残念！正解は {secret_number} でした。")

if __name__ == "__main__":
    main()
