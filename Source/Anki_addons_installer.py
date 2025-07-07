import os
import shutil
import tkinter as tk
from tkinter import messagebox, simpledialog

ADDON_SRC = os.path.join(os.getcwd(), "addons")
ADDON_DST = os.path.join(os.getenv("APPDATA"), "Anki2", "addons21")

def copy_addon(addon_name):
    src = os.path.join(ADDON_SRC, addon_name)
    dst = os.path.join(ADDON_DST, addon_name)
    shutil.copytree(src, dst, dirs_exist_ok=True)

def on_submit():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Bạn chưa chọn addon.")
        return
    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn cài Addon vừa chọn?")
    if not confirm:
        return
    for i in selected:
        addon = listbox.get(i)
        try:
            copy_addon(addon)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cài {addon}: {e}")
    messagebox.showinfo("Xong", "Đã sao chép addon thành công.")

root = tk.Tk()
root.title("Trình cài Addons Anki")

tk.Label(root, text="Chọn addon muốn cài:").pack()
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=40)
listbox.pack()

if os.path.exists(ADDON_SRC):
    for item in os.listdir(ADDON_SRC):
        if os.path.isdir(os.path.join(ADDON_SRC, item)):
            listbox.insert(tk.END, item)
else:
    messagebox.showerror("Lỗi", f"Không tìm thấy thư mục addons\n{ADDON_SRC}")
    root.destroy()

tk.Button(root, text="Cài đặt", command=on_submit).pack(pady=10)
root.mainloop()
