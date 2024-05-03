import tkinter as tk
import random

class SlotGame:
    def __init__(self, master):
        self.master = master
        self.master.title("スロットゲーム")

        # スロットの絵柄
        self.symbols = ["🍒", "🍋", "🍇", "🍀", "🔔", "💎"]

        # リールの初期状態
        self.reels = [random.choice(self.symbols) for _ in range(3)]

        # ラベルでリールを表示
        self.reel_labels = []
        for i in range(3):
            reel_label = tk.Label(master, text=self.reels[i], font=("Arial", 50))
            reel_label.grid(row=0, column=i)
            self.reel_labels.append(reel_label)

        # スタートボタン
        self.start_button = tk.Button(master, text="スタート", command=self.start_spin)
        self.start_button.grid(row=1, columnspan=3)

    def start_spin(self):
        # スタートボタンを無効化
        self.start_button.config(state="disabled")
        # リールを回転
        self.spin_reels()

    def spin_reels(self):
        # リールをランダムに回転させる
        for i in range(3):
            self.reels[i] = random.choice(self.symbols)
        self.update_reels()
        # 80ミリ秒ごとにリールを更新する
        self.update_id = self.master.after(80, self.spin_reels)

    def update_reels(self):
        # リールの表示を更新する
        for i in range(3):
            self.reel_labels[i].config(text=self.reels[i])

    def stop_reels(self):
        # リールを停止
        self.master.after_cancel(self.update_id)
        # スタートボタンを有効化
        self.start_button.config(state="normal")

root = tk.Tk()
game = SlotGame(root)

# ストップボタン
stop_button = tk.Button(root, text="ストップ", command=game.stop_reels)
stop_button.grid(row=2, columnspan=3)

root.mainloop()