import tkinter as tk
from tkinter import messagebox
import time
import random

# Fungsi utama untuk pencarian subset secara exhaustive secara urut
def exhaustive_subsets(arr, current_subset, index, target, steps, result, subset_size):
    if len(current_subset) == subset_size:
        current_sum = sum(current_subset)

        if current_sum == target:
            steps.append(f"Subset found: {current_subset}, Sum: {current_sum}*")
            result.append(list(current_subset))
            return
        else:
            if current_sum < target:
                steps.append(f"Current Subset: {current_subset}, Sum: {current_sum}")
            else:
                steps.append(f"Current Subset: {current_subset}, Sum: {current_sum} (sum exceeds target)")

    for i in range(index, len(arr)):
        current_subset.append(arr[i])
        exhaustive_subsets(arr, current_subset, i + 1, target, steps, result, subset_size)
        current_subset.pop()

# Fungsi untuk memulai proses pencarian subset
def find_subsets(arr, target):
    steps = []
    result = []
    subsets = []
    index = 0
    subset_size = 0
    start_time = time.time()
    for subset_size in range(len(arr) + 1):
        steps.append(f"Subset Size : {subset_size}")
        exhaustive_subsets(arr, subsets, index, target, steps, result, subset_size)
        steps.append(f"\n")
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

        random_subsets_label = tk.Label(result_window, text="Random Subset found:")
        random_subsets_label.pack()

        # Ambil subset acak dari himpunan solusi yang ditemukan
        random_subset = random.choice(result)
        subset_label = tk.Label(result_window, text=str(random_subset))
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