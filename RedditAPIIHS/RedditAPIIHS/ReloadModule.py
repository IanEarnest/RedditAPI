
import RedditAPIIHS
import importlib

# Show current time %H:%M:%S
def CurrentTime():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

# Return string with the current time
def UpdateWelcomeMessageTime():
    return f"""Welcome to RedditAPI - {CurrentTime()}\n
    - 0 = quit \n
    - 1 = reddit.com/r/all/.json?limit=5 \n
    enter url: \n"""

# Keep requesting user input, perform tasks based on input and reloads module
# e.g. input: 1, output: (request to reddit.com)
#
def MainLoop():
    welcomeMessage = UpdateWelcomeMessageTime()
    userInput = input(welcomeMessage)

    while userInput != "0":
        if userInput == "1" or userInput == "reddit.com":
            print("Requesting reddit.com/r/all/.json?limit=5...")
            RedditAPIIHS.RequestGet("https://reddit.com/r/all/.json?limit=5")
        elif userInput == "":
            #RedditAPIIHS.Testing()
            print("Reloading...")
        else:
            print(f"Requesting {userInput}...")
            RedditAPIIHS.RequestGet(f"{userInput}")

        importlib.reload(RedditAPIIHS) # keep up to date with code changes
        print("-----------------\n\n")

        welcomeMessage = UpdateWelcomeMessageTime()
        userInput = input(welcomeMessage) # keep checking user input