# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, scrolledtext
import re  # 导入正则表达式模块

class Guess:
    def __init__(self):
        self.sum = 0.0
        self.order = [0] * 100

    def __str__(self):
        progress = []
        for i in range(1, len(self.order)):
            if self.order[i] == 0 and i != 0:
                break
            if i % 4 == 0 and i != 0:
                progress.append(f"{self.order[i]}\n")
            else:
                progress.append(f"{self.order[i]}  ::  ")

        answer = "".join(progress) + f"\n\n总计长度为: {self.sum}"
        return answer

class GuessMVC(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("坯布计数器")
        self.geometry("400x370")

        self.guess = Guess()

        self.label1 = tk.Label(self, text="请在方框中输入多卷坯布的长度", font=("Arial", 20))
        self.label1.pack(pady=10)

        self.text = scrolledtext.ScrolledText(self, width=40, height=10)
        self.text.pack(pady=10)

        self.submit_button = tk.Button(self, text="提交", command=self.submit)
        self.submit_button.pack(side=tk.LEFT, padx=40)

        self.remake_button = tk.Button(self, text="重置", command=self.remake)
        self.remake_button.pack(side=tk.RIGHT, padx=40)

    def submit(self):
        try:
            # 获取输入的内容
            input_data = self.text.get("1.0", tk.END)

            # 使用正则表达式提取所有数字（包括整数和小数）
            numbers = re.findall(r'\d+\.?\d*', input_data)

            # 将提取的数字转换为浮点数
            numbers = list(map(float, numbers))

            self.guess.sum = 0.0
            i = 1
            for number in numbers:
                if i < len(self.guess.order):
                    self.guess.order[i] = number
                    self.guess.sum += number
                    i += 1

            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, str(self.guess))

        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字！")
        except Exception as e:
            messagebox.showerror("错误", f"发生错误: {str(e)}")

    def remake(self):
        self.text.delete("1.0", tk.END)
        self.guess.sum = 0.0
        self.guess.order = [0] * 100

if __name__ == "__main__":
    app = GuessMVC()
    app.mainloop()
