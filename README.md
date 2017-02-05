# twitch-logger
Logs chat messages of [twitch.tv](twitch.tv) user. To be used in the future to imitate users messaging style.

For each user you want to log all channels that the user follows is checked to see if they are chatting. If they send a message it is logged in file for only that user in that channel.

##Usage
CFG Requirements:

* NAME as Username of your bot
* PASS as OAuth password (Can be generated [here](https://twitchapps.com/tmi/))

Create a new UserManager() with a list of users as strings as the only argument.

```
manager = UserManager(["justin","clintstevens","northernlion"])
```

Main file contains what is required, excluding the list of users.

Files are then logged to folders of each user in textfiles for each channel.

##TO DO

* Let channel readers sleep if channel offline
* Let channel sleep if no user that follows that channel is in the chat

##To Note
This repo was remade becuase the previous one contained sensitive information.

**Author:** Benjamin Friesen

**E-mail:** bfriesen95@gmail.com
