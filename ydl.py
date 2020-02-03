#!/usr/bin/python3
import os
import time
import pafy
from subprocess import PIPE, run
from colors import colors
colors = colors()


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


def valid_path(userpath):
    exist = os.path.exists(userpath)
    if(exist):
        print(colors.BGreen+"\npath is valid"+colors.nocolor)
        return str(userpath)
    else:
        print(colors.BRed+"enter valid path:"+colors.nocolor)
        path = input()
        return valid_path(path)


def check(choice, mode):
    if mode == 1:
        if choice == "1":
            single_download()

        if choice == "2":
            playlist_download()
        if choice == "3":
            exit()
        else:
            choice = input(colors.BRed+"enter a valid choice:"+colors.nocolor)
            check(choice, mode=1)
    if mode == 2:
        if choice == "1":
            return 1
        if choice == "2":
            return 2
        if choice == "3":
            return 3
        if choice == "4":
            exit()
        else:
            choice = input(colors.BRed+"enter a valid choice:"+colors.nocolor)
            check(choice, mode=2)


def single_download():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    os.system("toilet -f future -F metal Single Video Download -t")
    print("-"*50)
    surl = input(colors.Blue+"Enter URL:"+colors.BGreen)
    try:
        metadata = pafy.new(surl, basic=True)
        print("\n"+colors.BYellow)
        os.system("ytdl "+surl)
    except ValueError:
        print("enter a valid youtube url")
        time.sleep(1)
        single_download()
    print("\n"+colors.BWhite)
    print(metadata)
    print("\n")
    os.system("toilet -f emboss -F metal MENU -t")
    print(colors.BGreen+"\n1)Download Best Video Quality")
    print(colors.BYellow+"2)Download Audio only (with best Quality)")
    print(colors.BBlue+"3)Other Formats")
    print(colors.BPurple+"4)Exit")
    choice = input(colors.Cyan+"\nenter choice:"+colors.BGreen)
    ret = check(choice, mode=2)
    userpath = input("enter path to save video:")
    correct_path = valid_path(userpath)
    os.chdir(correct_path)
    if ret == 1:
        print(colors.BPurple)
        os.system("ytdl -b "+surl)
    if ret == 2:
        os.system("ytdl -a "+surl)
    if ret == 3:
        while(True):
            n = input(colors.BCyan+"select a number from the above streams list:")
            resp = out("ytdl -n "+n+" "+surl+" &")
            resp = str(resp)
            if "Sorry" in resp:
                print(resp)
            else:
                os.system("ytdl -n "+n+" "+surl)
                break
    input("Thank You for using the script :)")
    input(colors.Blue+"press any key to exit!"+colors.nocolor)
    exit()


def playlist_download():
    if os.name == "nt":
        os.sytem("cls")
    else:
        os.system("clear")
    os.system("toilet -f future -F metal Playlist Download -t")
    print("-"*50)
    purl = input(colors.Blue+"Enter Playlist URL:"+colors.BGreen)
    try:
        playlist = pafy.get_playlist2(purl, basic=True)
        print("-"*50)
        print(playlist)
    except ValueError:
        print(colors.BRed+"enter a valid Playlist URL..")
        time.sleep(1)
        playlist_download()
    print("-"*50)
    print(colors.BGreen+"\n1)Download Best Video Quality")
    print(colors.BYellow+"2)Download Audio only (with best Quality)")
    print(colors.BBlue+"3)Make A file with all downloadable links")
    print(colors.BPurple+"4)Exit")
    choice = input(colors.Cyan+"\nenter choice:"+colors.BGreen)
    ret = check(choice, mode=2)
    userpath = input(colors.BPurple+"enter path to save the playlist:")
    correct_path = valid_path(userpath)
    os.chdir(correct_path)
    count = 0
    os.system("toilet -f mini -F gay DOWNLOADING!!")
    if ret != 3:
        for item in range(len(playlist)):
            count = count + 1
            if ret == 1:
                print(f"downloading VIDEO:{count}")
                url = playlist[item].getbest()
            if ret == 2:
                print(f"downloading audio in VIDEO:{count}")
                url = playlist[item].getbestaudio()
            url.download(userpath)
            # time.sleep(3)  # just to not make immediate download call
    else:
        file = open("links.txt", "w")
        for item in range(len(playlist)):
            count = count + 1
            print(f"adding links of VIDEO:{count}")
            link = playlist[item].getbest().url
            file.write("***********************************************************\n")
            file.write("link of Video:"+str(count))
            file.write("\n")
            file.write("***********************************************************\n")
            file.write("video Details:\n")
            file.write(str(playlist[item]))
            file.write("############################################################\n")
            file.write("\n")
            file.write(link)
            file.write("\n")
            file.write("\n############################################################")
        file.close()

    print("Downloads completed!!!!!")
    print(colors.BGreen+"Thank You for using the script :)")
    input(colors.Blue+"press any key to exit!"+colors.nocolor)
    exit()


if __name__ == "__main__":
    os.system("clear")
    os.system("toilet -f big -F gay YT DOWNLOADER -t")
    print(colors.BPurple+"--->written by @rohith.vishaal\n"+colors.nocolor)
    os.system("toilet -f emboss -F metal MENU -t")
    print(colors.BGreen+"\n1)Single Video Download")
    print(colors.BYellow+"2)playlist Download")
    print(colors.BPurple+"3)Exit")
    choice = input(colors.Cyan+"\nenter choice:")
    check(choice, mode=1)
