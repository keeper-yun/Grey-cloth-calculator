import tkinter as tk
from tkinter import scrolledtext, messagebox
from decimal import Decimal, getcontext, InvalidOperation
import math


def find_multiplication_pairs(target_str: str):
    """
    接收一个字符串格式的数字，找出所有符合以下条件的乘数组合：
    1. 一个一位小数(A)乘以一个两位小数(B)等于目标数字。
    2. 一位小数(A)的整数部分不为0 (A >= 1.0)。
    3. 两位小数(B)的整数部分为1位 (0 < B < 100.00)。

    Args:
        target_str: 字符串格式的目标数字，例如 "57002.94"。

    Returns:
        一个包含所有可能解的列表。每个解是一个元组，包含两个字符串格式的数字。
        
    Raises:
        ValueError: 如果输入字符串无效或不符合要求。
    """
    try:
        # 设置Decimal的精度
        getcontext().prec = 50
        target_decimal = Decimal(target_str)

        if target_decimal.quantize(Decimal('0.01')) != target_decimal:
            raise ValueError("错误：输入的金额小数位数必须是两位。")

    except InvalidOperation:
        raise ValueError(f"输入无效: '{target_str}' 不是一个有效的数字。")

    # 将问题转换为整数因数分解： a * b = target * 1000
    target_int = int(target_decimal * 1000)

    if target_int <= 0:
        raise ValueError("请输入一个大于零的数字。")

    solutions = []
    solution_set = set()  # 用于去重

    # 遍历到 target_int 的平方根以找到所有因数对
    for i in range(1, int(math.sqrt(target_int)) + 1):
        if target_int % i == 0:
            factor1 = i
            factor2 = target_int // i

            # 解法1: factor1 -> 一位小数, factor2 -> 两位小数
            # 一位小数 A >= 1.0  => factor1 >= 10
            # 两位小数 B < 100.00 => factor2 < 10000
            if factor1 >= 10 and factor2 < 10000:
                num1_str = f"{(Decimal(factor1) / 10):.1f}"
                num2_str = f"{(Decimal(factor2) / 100):.2f}"
                # 两位小数必须大于0
                if Decimal(num2_str) > 0:
                    solution_tuple = (num1_str, num2_str)
                    if solution_tuple not in solution_set:
                        solutions.append(solution_tuple)
                        solution_set.add(solution_tuple)

            # 解法2: factor2 -> 一位小数, factor1 -> 两位小数
            # 一位小数 A >= 1.0  => factor2 >= 10
            # 两位小数 B < 100.00 => factor1 < 10000
            if factor2 >= 10 and factor1 < 10000 and factor1 != factor2:
                num1_swap_str = f"{(Decimal(factor2) / 10):.1f}"
                num2_swap_str = f"{(Decimal(factor1) / 100):.2f}"
                # 两位小数必须大于0
                if Decimal(num2_swap_str) > 0:
                    solution_tuple_swap = (num1_swap_str, num2_swap_str)
                    if solution_tuple_swap not in solution_set:
                        solutions.append(solution_tuple_swap)
                        solution_set.add(solution_tuple_swap)

    return solutions


def create_gui():
    """
    创建并运行程序的GUI界面。
    """
    window = tk.Tk()
    window.title("乘数组合计算器")
    window.geometry("600x450")

    main_frame = tk.Frame(window, padx=10, pady=10)
    main_frame.pack(fill=tk.BOTH, expand=True)

    input_frame = tk.Frame(main_frame)
    input_frame.pack(fill=tk.X)

    label = tk.Label(input_frame, text="请输入一个总金额:")
    label.pack(side=tk.LEFT, pady=5)

    entry = tk.Entry(input_frame, width=20)
    entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    result_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
    result_text.pack(pady=10, fill=tk.BOTH, expand=True)
    result_text.config(state=tk.DISABLED)

    def calculate_and_display(event=None):
        target_str = entry.get()
        if not target_str:
            messagebox.showwarning("输入为空", "请输入一个总金额。")
            return

        try:
            solutions = find_multiplication_pairs(target_str)

            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)

            if not solutions:
                result_text.insert(tk.END, f"未能为 {target_str} 找到任何符合条件的乘数组合。")
            else:
                result_text.insert(tk.END, f"为 {target_str} 找到了 {len(solutions)} 组可能的结果：\n\n")

                limit = 200
                for i, (num1, num2) in enumerate(solutions[:limit]):
                    result_text.insert(tk.END, f"   {num1} (米数) × {num2} (金额) = {target_str}\n")

                if len(solutions) > limit:
                    result_text.insert(tk.END, f"\n... 以及另外 {len(solutions) - limit} 组结果未显示。")

        except ValueError as e:
            messagebox.showerror("输入错误", str(e))
        except Exception as e:
            messagebox.showerror("未知错误", f"发生了一个未知错误: {e}")
        finally:
            result_text.config(state=tk.DISABLED)

    entry.bind("<Return>", calculate_and_display)

    button = tk.Button(input_frame, text="计算", command=calculate_and_display)
    button.pack(side=tk.LEFT, padx=5)

    window.mainloop()


def main():
    """
    程序主函数，用于启动GUI。
    """
    create_gui()


if __name__ == "__main__":
    main()
