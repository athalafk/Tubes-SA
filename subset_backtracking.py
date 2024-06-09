import tkinter as tk
from tkinter import messagebox
import time

# Fungsi utama untuk pencarian subset secara backtracking
def backtracking_subsets(index, target, matrix, arr, steps, result):
    current_subset = [arr[i] for i in range(len(matrix)) if matrix[i] == 1]
    current_sum = sum(current_subset)

    # Jika sum saat ini sama dengan target, simpan hasil dan hentikan pencarian
    if current_sum == target:
        steps.append(f"Subset found: {current_subset}, Sum: {current_sum}")
        result.append(current_subset)
        return

    # Jika sum saat ini sudah lebih dari target, hentikan branch ini
    if current_sum > target:
        steps.append(f"Kill branch: Current Subset: {current_subset}, Sum: {current_sum} (sum exceeds target)")
        return

    if index < len(arr):
        # Jika termasuk elemen arr[index]
        matrix[index] = 1
        steps.append(f"Include {arr[index]}, Current Subset: {current_subset + [arr[index]]}, Sum: {current_sum + arr[index]}")
        if current_sum + arr[index] < target:
            steps.append(f"Check branch: Current Subset: {current_subset + [arr[index]]}, Sum: {current_sum + arr[index]} (sum less than target)\n")
        backtracking_subsets(index + 1, target, matrix, arr, steps, result)
        
        if result:  # Jika solusi ditemukan dalam rekursi, hentikan pencarian
            return
        
        # Jika tidak termasuk elemen arr[index]
        matrix[index] = 0
        steps.append(f"Exclude {arr[index]}, Current Subset: {current_subset}, Sum: {current_sum}\n")
        backtracking_subsets(index + 1, target, matrix, arr, steps, result)

def find_subsets(arr, target):
    matrix = [0] * len(arr)
    steps = []
    result = []
    index = 0
    start_time = time.time()
    backtracking_subsets(index, target, matrix, arr, steps, result)
    end_time = time.time()
    execution_time = end_time - start_time
    return steps, result, execution_time

# Fungsi untuk menampilkan hasil di GUI
def display_results(root, entry_arr, entry_target):
    arr = list(map(int, entry_arr.get().split(',')))
    target = int(entry_target.get())

    steps, result, execution_time = find_subsets(arr, target)

    if not result:
        messagebox.showinfo("Result", "No subset found")
    else:
        result_window = tk.Toplevel(root)
        result_window.title("Subset Sum Steps")

        text = tk.Text(result_window, wrap='word')
        text.pack(expand=1, fill='both')

        for step in steps:
            text.insert('end', step + "\n")
        
        subset_label = tk.Label(result_window, text="Subsets found:")
        subset_label.pack()

        for subset in result:
            subset_label = tk.Label(result_window, text=str(subset))
            subset_label.pack()

        time_label = tk.Label(result_window, text=f"Execution time: {execution_time:.6f} seconds")
        time_label.pack()

# Fungsi untuk setup GUI
def setup_GUI():
    root = tk.Tk()
    root.title("Subset Sum Problem")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label_arr = tk.Label(frame, text="Enter subsets (comma-separated):")
    label_arr.grid(row=0, column=0, pady=5)

    entry_arr = tk.Entry(frame, width=50)
    entry_arr.grid(row=0, column=1, pady=5)

    label_target = tk.Label(frame, text="Enter target sum:")
    label_target.grid(row=1, column=0, pady=5)

    entry_target = tk.Entry(frame, width=50)
    entry_target.grid(row=1, column=1, pady=5)

    button_solve = tk.Button(frame, text="Solve", command=lambda: display_results(root, entry_arr, entry_target))
    button_solve.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

# Panggil fungsi setup_GUI untuk memulai aplikasi
setup_GUI()