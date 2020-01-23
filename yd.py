
import pafy
import os
from colors import colors
import time
colors = colors()
# import sys
# import time
# url = sys.argv[1]  # takes the playlist link as argument


def playlist():
    os.system("clear")
    os.system("toilet -f big -F gay YT DOWNLOADER -t")
    print(colors.BPurple+"-----------------written by @rohith.vishaal-------------------"+colors.nocolor)
    url = input("enter playlist url:")
    details = pafy.get_playlist(url)
    playlist = pafy.get_playlist2(url)
    # below three statements print the tilte,author and number of videos
    print("----------------------------------------------------------------------")
    print(f"\ntitle of playlist:{details['title']}\n")
    print(f"author of the playlist:{details['author']}\n")
    print(f"number of videos in the playlist:{len(playlist)}\n\n")
    # path to store the videos
    userpath = input("enter path to save the playlist:")
    # you can modify this for loop for a particular range of videos
    # this a bare-bone
    # this loop downloads all the videos in the playlist
    count = 0
    os.system("figlet -f mini DOWNLOADING!!")
    for item in range(len(playlist)):
        count = count + 1
        print(f"downloading VIDEO:{count}")
        print(playlist[item].get_filesize())
        # url = playlist[item].getbest()
        url.download(userpath)
        # time.sleep(3)  # just to not make immediate download calls
    print("Downloads completed!!!!!")
    input("press any key to exit!")
    exit()


if __name__ == "__main__":
    playlist()
