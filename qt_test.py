import sys
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtCore import QUrl, pyqtSignal, QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.box = QVBoxLayout(self)
        self.web = MyWebEngineView()  # 创建浏览器组件对象
        self.web.cookieSignal.connect(self.handleCookie)  # 连接信号
        self.web.resize(1280, 720)
        self.web.load(QUrl("https://music.163.com/#/login"))
        self.box.addWidget(self.web)
        self.cookie_value = None  # 初始化变量

    def handleCookie(self, value):
        self.cookie_value = value  # 存储cookie的值
        QApplication.instance().quit()  # 退出应用程序


class MyWebEngineView(QWebEngineView):
    # 定义一个信号
    cookieSignal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(MyWebEngineView, self).__init__(*args, **kwargs)
        # 清空所有Cookies
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
        # 绑定cookie被添加的信号槽
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(
            self.onCookieAdd
        )
        self.cookies = {}

    def onCookieAdd(self, cookie: QNetworkCookie):
        name = cookie.name().data().decode("utf-8")
        value = cookie.value().data().decode("utf-8")
        self.cookies[name] = value
        if name == "MUSIC_U":
            # 发出信号并传递 value 值
            self.cookieSignal.emit(value)


def login() -> dict:
    app = QApplication(sys.argv)
    w = Window()
    w.show()

    # 自定义事件循环
    loop = QEventLoop()
    w.destroyed.connect(loop.quit)
    loop.exec_()

    # 在事件循环退出后输出 cookie 的值
    return {"MUSIC_U": w.cookie_value}
