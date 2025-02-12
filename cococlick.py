import pyautogui
import time
import csv

def cococlick():
    positions_file = 'clicks.csv'
    click_data = []

    try:
        with open(positions_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # ヘッダーをスキップ
            for row in reader:
                try:
                    x_val = int(row[0])
                    y_val = int(row[1])
                    interval = float(row[2])  # クリック間隔を取得
                    click_data.append((x_val, y_val, interval))
                except ValueError:
                    print(f"Invalid data in row: {row}")
                    continue
    except FileNotFoundError:
        print(f"File not found: {positions_file}")
        return

    print(f"クリックデータ: {click_data}")

    for x, y, interval in click_data:
        print(f"Clicking at: ({x}, {y}) after {interval} seconds")
        time.sleep(interval)  # 記録された間隔で待機
        pyautogui.click(x, y)

if __name__ == "__main__":
    cococlick()