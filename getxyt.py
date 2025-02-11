import csv
import time
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key

# クリック位置と間隔を記録するリスト
click_data = []
mouse_listener = None  # マウスリスナーを外部からアクセス可能にするため
last_click_time = None  # 前回のクリック時刻を記録

# クリック時に呼び出される関数
def on_click(x, y, button, pressed):
    global last_click_time
    if pressed:
        current_time = time.time()
        interval = current_time - last_click_time if last_click_time else 0  # 初回は0
        last_click_time = current_time

        x_int = int(x)
        y_int = int(y)
        print(f'{x_int}, {y_int}, 間隔: {interval:.3f}秒')

        click_data.append((x_int, y_int, round(interval, 3)))  # 位置と時間間隔を記録

# キー押下時に呼び出される関数（qキーでリスナー終了）
def on_press(key):
    if key.char == 'q':
        print("qキーが押されました。リスナーを終了します。")
        if mouse_listener is not None:
            mouse_listener.stop()  # マウスリスナーを終了
        return False  # キーボードリスナーを終了

# マウスリスナーを開始
with MouseListener(on_click=on_click) as listener:
    mouse_listener = listener  # マウスリスナーをグローバル変数に格納

    # キーボードリスナーを別スレッドで開始
    with KeyboardListener(on_press=on_press) as keyboard_listener:
        keyboard_listener.join()  # qキーが押されるのを待機

# リスナー終了後、CSVに書き込む
with open('click_positions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X', 'Y', 'Interval'])  # ヘッダーを追加
    writer.writerows(click_data)  # 全データを書き込む

print("クリック位置と間隔をCSVに書き込みました。")
