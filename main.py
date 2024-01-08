import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from loginQT import Ui_LoginForm as LoginForm
from registerQT import Ui_RegisterForm as RegisterForm
from passwordQT import Ui_PasswordForm as PasswordForm
from listQT import Ui_ToDoListForm as ToDoListForm

class DraggableWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.offset = None
        self.mouse_pressed = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mouse_pressed = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            self.move(self.mapToParent(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mouse_pressed = False
            self.offset = None

class TransparentWidget(DraggableWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class TitleBar(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, 5, parent.width(), 30)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.title_layout = QtWidgets.QHBoxLayout(self)
        self.title_layout.setContentsMargins(0, 0, 0, 0)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setContentsMargins(5, 0, 0, 0)

        self.close_button = QtWidgets.QPushButton("X", self)
        self.minimize_button = QtWidgets.QPushButton("—", self)

        self.close_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgba(0, 0, 0, 200);")
        self.minimize_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgba(0, 0, 0, 200);")

        self.close_button.clicked.connect(parent.close)
        self.minimize_button.clicked.connect(parent.showMinimized)

        self.close_button.installEventFilter(self)
        self.minimize_button.installEventFilter(self)

        button_layout.addWidget(self.minimize_button)
        button_layout.addWidget(self.close_button)

        self.title_layout.addStretch(1)
        self.title_layout.addLayout(button_layout)

        self.mouseMoveEvent = parent.mouseMoveEvent
        self.mousePressEvent = parent.mousePressEvent

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Enter:
            source.setStyleSheet("background-color: rgba(50, 50, 50, 100); color: rgba(255, 255, 255, 200);")
        elif event.type() == QtCore.QEvent.Leave:
            source.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgba(0, 0, 0, 200);")

        return super().eventFilter(source, event)


class LoginRegisterApp(TransparentWidget):
    def __init__(self):
        super().__init__()

        # İlk olarak giriş sayfasını oluştur
        self.login_page = TransparentWidget()
        self.ui_login = LoginForm()
        self.ui_login.setupUi(self.login_page)
        self.setup_title_bar(self.login_page)

        # Şifremi Unuttum sayfasını oluştur
        self.password_page = TransparentWidget()
        self.ui_password = PasswordForm()
        self.ui_password.setupUi(self.password_page)
        self.setup_title_bar(self.password_page)

        # Kayıt sayfasını oluştur
        self.register_page = TransparentWidget()
        self.ui_register = RegisterForm()
        self.ui_register.setupUi(self.register_page)
        self.setup_title_bar(self.register_page)

        # Liste sayfasını oluştur
        self.list_page = TransparentWidget()
        self.ui_list = ToDoListForm()
        self.ui_list.setupUi(self.list_page)
        self.setup_title_bar(self.list_page)

        # Giriş sayfasındaki "Giriş" butonuna bağlı fonksiyonu tanımla
        self.ui_login.pushButton_giris.clicked.connect(self.login_and_open_list)

        # Giriş sayfasındaki "Kayıt Ol" butonuna bağlı fonksiyonu tanımla
        self.ui_login.pushButton_kayitol.clicked.connect(self.open_register_page)

        # Giriş sayfasındaki "Şifremi Unuttum" butonuna bağlı fonksiyonu tanımla
        self.ui_login.commandLinkButton_sifremiunuttum.clicked.connect(self.open_password_page)

        # Şifremi Unuttum sayfasındaki "Onayla" butonuna bağlı fonksiyonu tanımla
        self.ui_password.pushButton_onayla.clicked.connect(self.return_to_login_page)

        # Kayıt sayfasındaki "Kayıt Ol" butonuna bağlı fonksiyonu tanımla
        self.ui_register.pushButton_kayitol_2.clicked.connect(self.register_and_back)

        # Uygulamayı başlat
        self.login_page.show()
        
    def setup_title_bar(self, page_widget):
        title_bar = TitleBar(page_widget)
        page_layout = QtWidgets.QVBoxLayout(page_widget)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(title_bar)
        title_bar.title_layout.setAlignment(QtCore.Qt.AlignTop)

    def open_register_page(self):
        # "Kayıt Ol" butonuna tıklandığında kayıt sayfasına geç
        self.register_page.show()
        self.login_page.hide()

    def open_password_page(self):
        # "Şifremi Unuttum" butonuna tıklandığında şifre sayfasına geç
        self.password_page.show()
        self.login_page.hide()

    def return_to_login_page(self):
        # "Onayla" butonuna tıklandığında giriş sayfasına geri dön
        self.login_page.show()
        self.password_page.hide()

    def register_and_back(self):
        # Kayıt işlemi tamamlandıktan sonra giriş sayfasına geri dön
        self.login_page.show()
        self.register_page.hide()

    def login_and_open_list(self):
        # Giriş işlemi tamamlandıktan sonra liste sayfasını aç
        self.list_page.show()
        self.login_page.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = LoginRegisterApp()
    sys.exit(app.exec_())
