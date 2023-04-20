import tkinter as tk
import time

class ChatRoom(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 建立聊天室視窗
        self.chat_log = tk.Text(self, state="disabled", width=50, height=20)
        self.chat_log.grid(row=0, column=0, columnspan=2)

        # 建立A的輸入框
        self.input_a = tk.Entry(self, width=40)
        self.input_a.grid(row=1, column=0)

        # 建立A送出訊息的按鈕
        self.send_a = tk.Button(self, text="A送出", command=self.send_message_a)
        self.send_a.grid(row=1, column=1)

        # 建立B的輸入框
        self.input_b = tk.Entry(self, width=40)
        self.input_b.grid(row=2, column=0)

        # 建立B送出訊息的按鈕
        self.send_b = tk.Button(self, text="B送出", command=self.send_message_b)
        self.send_b.grid(row=2, column=1)

        self.input_a.bind("<Return>", lambda event: self.send_message_a())
        self.input_b.bind("<Return>", lambda event: self.send_message_b())

    def send_message_a(self):
        # 獲取A的訊息
        message = self.input_a.get()
        if message:
            # 將訊息加入聊天室視窗中
            self.chat_log.tag_config("green", background="light green")
            self.chat_log.configure(state="normal")
            self.chat_log.insert("end", "\n" ,"green")
            
            #多行
            for char in message:
                self.chat_log.insert("end", char, "green")
                self.chat_log.see("end")
                self.chat_log.update()
                time.sleep(0.03)
            self.chat_log.insert("end", "\n\n", "green")
            self.chat_log.see("end")            
            self.chat_log.configure(state="disabled")

            # 清空A的輸入框
            self.input_a.delete(0, "end")

    def send_message_b(self):
        # 獲取B的訊息
        message = self.input_b.get()
        if message:
            # 將訊息加入聊天室視窗中
            self.chat_log.tag_config("orange", background="light salmon")
            self.chat_log.configure(state="normal")
            self.chat_log.insert("end", "\n" ,"orange")

            for char in message:
                self.chat_log.insert("end", char, "orange")
                self.chat_log.see("end")
                self.chat_log.update()
                time.sleep(0.02)
            self.chat_log.insert("end", "\n\n", "orange")
            self.chat_log.see("end")
            self.chat_log.configure(state="disabled")

            # 清空B的輸入框
            self.input_b.delete(0, "end")

# 建立主視窗
root = tk.Tk()
root.title("聊天室")

# 建立聊天室
chatroom = ChatRoom(master=root)
chatroom.mainloop()
