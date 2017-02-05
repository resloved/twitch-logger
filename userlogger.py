from cfg import ID, API
from bot import Bot
from util import addToList
import requests

# Contain bots for channels
# Contains users with list of channels
class UserManager:

    def __init__(self, users):

        # Store users
        self.bots = []
        self.users = []
        self.addUser(users)

        # Start bots
        self.setupBots()

        self.start()

    # Update -- [Bot restructuring may be needed. depends on future capab.]

    # [Seperate into smaller tasks]
    def setupBots(self):
        # Bot Setup
        # For each user to log..
        for user in self.users:
            # For each channel to follow..
            for chan in user.where():
                # Check if a bot is online
                found = False
                for bot in self.bots:
                    # Add target to bot if already online
                    if bot.chat == chan:
                        bot.addTarget(user.name)
                        found = True
                        break
                # Create new bot if not online
                if not found:
                    self.bots.append(Bot(chan, [user.name]))

    def start(self):
        while(True):
            for bot in self.bots:
                bot.read()

    def addUser(self,  toAdd):
        if isinstance(toAdd, list):
            for user in toAdd:
                self.users.append(User(user))
        else:
            self.users.append(User(toAdd))

    def startBot(self, name):
        pass

    # Task --

    # Main loop
    # - Check if bots can be added
    def Update():
        pass


# [just for chan storage]
# [might use for associted posting bot]
# [probably not because two functions will be seperated]
class User:

    def __init__(self, name, additional=None):
        self.following = []
        if additional is None:
            self.additional = []
        else:
            self.additional = additional
        self.name = name
        self.lookupFollowing()
        # collect channels
        # do api lookup
        pass

    # External --

    def where(self):
        places = []
        places.extend(self.following)
        places.extend(self.additional)
        return places

    # API --

    # [Add exceptions/errors for no followers and not a user]
    def lookupFollowing(self):

        url = "https://api.twitch.tv/kraken/users/{}/follows/channels" \
                .format(self.name)
        headers = {'Accept': API, 'Client-ID': ID}

        r = requests.get(url, headers=headers)
        data = r.json()
        for i in range(0, len(data["follows"])):
            self.following.append(data["follows"][i]["channel"]["name"])

    # Update --

    # [Currently only works with lists]
    def addChannel(self, names):
        for name in names:
            if name not in self.additional and name not in self.following:
                self.additional.append(name)

    # Task --

    # Main loop
    # - Update following
    # - Check if additional is changed?
    def Update():
        pass
