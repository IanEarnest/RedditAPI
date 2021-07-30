import requests
import ReloadModule

# MainModule - runs MainLoop for checking user input
# RedditAPIIHS - Reddit API calls
try:
    ReloadModule.MainLoop()
except Exception as e:
    print(f"Error occurred {e}")