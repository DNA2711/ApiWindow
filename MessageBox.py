import tkinter as tk
import ctypes
# import webbrowser
from tkinter import filedialog


class DevApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dev App")
        self.root.geometry("500x300")

        # Tạo các thành phần giao diện
        self.capture_button = tk.Button(
            root, text="Hiển thị thông báo", command=self.show_message)
        self.browser_button = tk.Button(
            root, text="Mở trình duyệt", command=self.open_browser)
        self.file_button = tk.Button(
            root, text="Mở File Explorer", command=self.open_file_dialog)
        self.quit_button = tk.Button(root, text="Thoát", command=root.quit)

        # Đặt các nút vào cửa sổ giao diện
        self.capture_button.pack(pady=10)
        self.browser_button.pack(pady=10)
        self.file_button.pack(pady=10)
        self.quit_button.pack(pady=10)

    def show_message(self):
        # Sử dụng API MessageBoxA của Windows để hiển thị thông báo
        user32 = ctypes.windll.user32
        MessageBox = user32.MessageBoxW

        MB_ICONINFORMATION = 0x40
        MB_OK = 0x0

        MessageBox(None, "TECH PYTHON SAVE THE WORLD",
                   "Thông báo", MB_ICONINFORMATION | MB_OK)

    def open_browser(self):
        # Sử dụng API ShellExecute để mở trình duyệt mặc định và mở URL
        url = "https://www.google.com"
        ctypes.windll.shell32.ShellExecuteW(None, "open", url, None, None, 1)

    def open_file_dialog(self):
        # Sử dụng thư viện filedialog để mở hộp thoại chọn tệp
        file_path = filedialog.askopenfilename()
        if file_path:
            print(f"Bạn đã chọn tệp: {file_path}")
        else:
            print("Bạn đã hủy việc chọn tệp.")


# Tạo cửa sổ giao diện và khởi chạy ứng dụng
if __name__ == "__main__":

    root = tk.Tk()
    app = DevApp(root)
    root.mainloop()
