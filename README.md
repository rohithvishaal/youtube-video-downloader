# youtube-video-downloader
It's a python script that helps you to download  a single youtube video or playlist and it also generates a downloadable link text file for playlist videos 


## Installation on Linux

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pafy and youtube-dl.

```bash
pip3 install pafy
pip3 install youtube-dl
```
Use apt to install **'toilet and figlet** an ascii font generating tool 

```bash
sudo apt-get install toilet
sudo apt-get install figlet
```


## Installation on TERMUX

You can download the Android App from here
[Termux App](https://play.google.com/store/apps/details?id=com.termux&hl=en_IN)


Use pkg to install **python** on Termux
```bash
pkg install python
```

Use pkg to install **'toilet and figlet** on termux app on android
```bash
pkg install toilet
pkg install figlet
```
Use  the Below command to link your phone storage because by default **Termux** cannot access your phone storage 
```bash
termux-setup-storage
```
The default path to the Downloads folder in your phone is
```bash
/storage/emulated/0/Download
```

## Setting your api key
[Information from Google about obtaining an API key](https://developers.google.com/youtube/registering_an_application)
## Usage

```python
python3 ydl.py
```

