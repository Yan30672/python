# 從tkinter匯入所有內建函數與模組
from tkinter import *;
# 下載與安裝pillow
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
# 下載符合python版本的pillow後，於cmd下(最高權限)，到pillow所在的路徑
# 執行pip install pillow-3.0.0-cp34-none-win32.whl(此pillow為python 3.4 32bit的3.0版本)
from PIL import Image, ImageTk


# 建立類別，Window，繼承Frame類別。Frame是一個類別，來自於tkinter模組，可參閱Lib/tkinter/__init__
class Window(Frame):  # 建立視窗實體
    # 初始化設定
    def __init__(self, master=None):
        Frame.__init__(self, master);  # 你想要透過Frame類別傳送的參數
        self.master = master;  # 參考到主要的小窗口，也就是tk視窗
        self.init_window();

    # 初始視窗的創建
    def init_window(self):
        # 改變我們主要的小窗口的標題
        self.master.title('GUI');
        # 允許小窗口去取得視窗的整個空間
        self.pack(fill=BOTH, expand=1);
        # 建立一個按鈕實體
        quitButton = Button(self, text='Quit');
        # 將按鈕放到視窗裡，座標為(10，10)
        quitButton.place(x=10, y=10);
        # 建立一個選單實體
        menu = Menu(self.master);
        self.master.config(menu=menu);
        # 建立檔案物件
        file = Menu(menu);
        # 添加一個命令到選單選項，呼叫它來離開，而命令，它在client_exit事件執行
        file.add_command(label='Exit', command=self.client_exit);
        # 添加一個File到選單
        menu.add_cascade(label='File', menu=file);
        # 建立檔案物件
        edit = Menu(menu);
        # 添加一個命令到選單選項，呼叫它來離開，而命令，它在client_exit事件執行
        edit.add_command(label='Undo');
        edit.add_command(label='Show Img', command=self.showImg);
        edit.add_command(label='Show Text', command=self.showText);
        # 添加Undo到選單
        menu.add_cascade(label='Edit', menu=edit);

    def client_exit(self):
        exit();

    def showImg(self):
        load = Image.open('20151211_tkinter.jpg');
        render = ImageTk.PhotoImage(load);
        # 標籤可以是文字或圖片
        img = Label(self, image=render);
        img.image = render;
        img.place(x=50, y=50);  # 將影像放入視窗裡，座標為(50，50)

    def showText(self):
        text = Label(self, text='成功呈現');
        text.pack();


# 視窗的建立，只會有一個，但是你可以在視窗裡建立小窗口
root = Tk();

# 視窗的大小
root.geometry('400x300');

app = Window(root);  # 建立一個實體

root.mainloop();  # 呈現它