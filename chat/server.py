from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
from threading import Thread


class User:
    def __init__(self, socket) -> None:
        self.socket = socket
        self.name = "Anonymous"

    def send(self, message):
        self.socket.send(message.encode("utf-8"))

    def receive(self, buffer_size):
        return self.socket.recv(buffer_size)

    def change_name(self, name):
        self.name = name


class Server:
    def __init__(
        self,
        name_protocol="name()",
        exit_protocol="exit()",
        online_protocol="online()",
        help_protocol="help()",
    ) -> None:
        self.host = "127.0.0.1"
        self.port = 33336
        self.buffer_size = 1024
        self.address = (self.host, self.port)
        self.name_protocol = name_protocol
        self.exit_protocol = exit_protocol
        self.online_protocol = online_protocol
        self.help_protocol = help_protocol
        self.users = []

    def up(self):
        self.run_socket()
        print("Waiting for connection...")
        self.start_thread()

    def down(self):
        self.socket.close()

    def run_socket(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(self.address)
        self.socket.listen(2)

    def start_thread(self):
        accept_thread = Thread(target=self.handle_connections)
        accept_thread.start()
        accept_thread.join()
        self.down()

    def handle_connections(self):
        while True:
            client, addr = self.socket.accept()
            print(f"A client has connected {addr}")
            Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        user = User(client)
        real_users_num, real_users_name = self.get_users()
        welcome_msg = f"Welcome {user.name}. there are {real_users_num} online registered user in chatroom. use Menu for more options."
        user.send(welcome_msg)
        chat_msg = f"{user.name} has joined the room"
        self.broadcast(chat_msg)
        self.users.append(user)

        while True:
            msg = user.receive(self.buffer_size)

            if msg == self.online_protocol.encode("utf8"):
                real_users_num, real_users_name = self.get_users()
                user.send(f"Online users {real_users_num} : {real_users_name}")
            elif self.name_protocol.encode("utf8") in msg:
                user.change_name(
                    msg.decode("utf8").replace(self.name_protocol + " ", "")
                )
            elif msg == self.exit_protocol.encode("utf8"):
                print(f"{user.name} has disconnected ")
                self.users.remove(user)
                self.broadcast(f"{user.name} has left the room!")
                break
            elif msg == self.help_protocol.encode("utf8"):
                instructions_msg = f"Type @<user-name> <your-message> to send private message to someone, e.g. @amir Hello"
                user.send(instructions_msg)
            elif "@".encode("utf8") in msg:
                self.unicast(msg, user)
            else:
                self.broadcast(f'{user.name}: {msg.decode("utf8")}')

    def broadcast(self, message):
        for user in self.users:
            user.send(message)

    def unicast(self, message, sender):
        message = message.decode("utf8")
        refered_user, user_msg = message.split(" ", 1)
        refered_user_name = refered_user.strip("@")
        for user in self.users:
            if user.name == refered_user_name:
                user.send(f"{sender.name} -> {refered_user_name}: {user_msg}")

    def get_users(self):
        real_users_num = 0
        real_users_name = []

        for user in self.users:
            if user.name != "Anonymous":
                real_users_num += 1
                real_users_name.append(user.name)

        return real_users_num, real_users_name


server = Server()
server.up()
