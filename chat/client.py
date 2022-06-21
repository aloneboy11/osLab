from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from signal import signal, SIGINT
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader


class Client(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        signal(SIGINT, self.handler)

        self.host = "127.0.0.1"
        self.port = 33336
        self.buffer_size = 1024
        self.address = (self.host, self.port)

        loader = QUiLoader()
        self.ui = loader.load("main.ui")
        self.change_name_ui = loader.load("change_name.ui")
        self.ui.show()

        self.ui.sendBtn.clicked.connect(self.send_msg)
        self.ui.input.returnPressed.connect(self.send_msg)

        self.chatModel = QStandardItemModel()
        self.ui.view.setModel(self.chatModel)

        self.ui.actionChange_name.triggered.connect(self.change_name_ui.show)
        self.ui.actionOnline.triggered.connect(self.show_online_users)
        self.ui.actionHelp.triggered.connect(self.show_instructions)
        self.ui.actionExit.triggered.connect(self.clean_exit)

        self.change_name_ui.saveBtn.clicked.connect(self.change_name)
        self.change_name_ui.nameInput.returnPressed.connect(self.change_name)

    def up(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(self.address)
        receive_thread = Thread(target=self.receive_msg)
        receive_thread.start()

    def receive_msg(self):
        while True:
            try:
                msg = self.socket.recv(self.buffer_size).decode("utf8")
                message = QStandardItem(msg)
                self.chatModel.appendRow(message)
                self.ui.view.scrollToBottom()
            except OSError as error:
                return error

    def send_msg(self, message=""):
        try:
            if type(message) != str or message == "":
                msg = self.ui.input.text()
                self.ui.input.clear()
            else:
                msg = message
            self.socket.send(msg.encode("utf8"))
        except EOFError:
            self.clean_exit()

    def change_name(self):
        name = self.change_name_ui.nameInput.text()
        if name != "":
            self.send_msg(f"name() {name}")
            self.change_name_ui.nameInput.clear()
            self.change_name_ui.close()
        else:
            self.change_name_ui.errorLabel.setText("name can not be empty")

    def show_instructions(self):
        self.send_msg("help()")

    def show_online_users(self):
        self.send_msg("online()")

    def clean_exit(self):
        self.socket.send("exit()".encode("utf8"))
        self.socket.close()
        sys.exit(0)

    def handler(self, signal_recv, frame):
        self.clean_exit()


app = QApplication([])
client = Client()
client.up()
app.aboutToQuit.connect(client.clean_exit)
app.exec()
