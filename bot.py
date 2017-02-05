from cfg import HOST, PORT, NICK, PASS
from util import addToList
import os
import socket
import re
import select


class Bot:

    # Setup --

    def __init__(self, chat, targets, timeout=1/20):

        # Format settings
        self.stalk = targets
        self.chat = chat.lower()
        self.targets = []
        self.addTarget(targets)
        [x.lower() for x in self.targets]

        # Check for target folders
        if isinstance(targets, list):
            for target in targets:
                self.makeDir(target)
        else:
            self.makeDir(targets)

        # Connect to channel
        self.s = socket.socket()
        self.timeout = timeout
        self.s.connect((HOST, PORT))
        self.s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
        self.s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
        self.s.send("JOIN {}\r\n".format("#" + self.chat).encode("utf-8"))
        print("-- Bot for {} ready --".format(self.chat))

    # Setup --

    def makeDir(self, name):
        if not os.path.exists(name):
            os.makedirs(name)

    def writeType(self, name):
        if not os.path.exists(name):
            return 'w'
        return 'a'

    # Parsing --

    def message(self, comment):
        comment_format = re.compile(
            r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
        return comment_format.sub("", comment)

    def username(self, comment):
        return re.search(r"\w+", comment).group(0)

    # Send --

    def ping(self):
        self.s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))

    # Update --

    def addTarget(self, toAdd):
        addToList(toAdd, self.targets)

    # Update --
    def read(self):
        while True:
            ready = select.select([self.s], [], [], self.timeout)
            if ready[0]:
                response = self.s.recv(1024).decode("utf-8")
                if response == "PING :tmi.twitch.tv\r\n":
                    self.ping()
                else:
                    user = self.username(response)
                    msg = self.message(response)
                    print("[{}] {}: {}".format("#" + self.chat, user, msg))
                    if user in self.targets:
                        # [Change to 'with']
                        fileName = "{}/{}".format(user, self.chat)
                        f = open(fileName, self.writeType(fileName))
                        f.write(msg)
                        f.close()
            else:
                break