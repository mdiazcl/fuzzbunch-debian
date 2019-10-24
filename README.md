![alt text](http://i.imgur.com/cexPDXR.png)

# Kali/fuzzbunch-debian deployment guide
NSA/Fuzzbunch deployment for kali linux - Intructions. This version was designed to work under kali linux (to enhance our personal pentesting tools) using wine (32bits version) since Fuzzbunch uses python26 and WindowsXP. This is very useful if you want to mix it with your Empire/Metasploit arsenal.

**This particular version of Fuzzbunch has some personal fixes that I found over the internet:**
 - Fuzzbunch.xml edited to be able to work on Wine
 - Fixed "listeningposts error" when running fb.py

## Motivation
I read a lot of different papers on how to install and run this on WindowsXP and a few running on Unix, none of them on Kali (Maybe there are a bunch, but I didn't do much research, to be honest). All of the they needed to fix some files, move folders, or download files from different websites, I just wanted to make it simple, quick and accessible for everyone only by typing a few bash commands and a git clone!

## Contact Info:
- **Email:** miguel.diaz {at} mdiazlira.com 
- https://twitter.com/mdiazcl

## Original Work and special thanks
- **ShadowBroker:** https://github.com/misterch0c/shadowbroker.git
- **Knightmare2600 Unix Guide:** https://github.com/knightmare2600/ShadowBrokers
- **Sheila Berta Paper:** https://www.exploit-db.com/docs/41897.pdf

## How to run?
**After you install** everything you can use fuzzbunch doing the following:
```
export WINEPREFIX=$HOME/.wine-fuzzbunch
cd $HOME/.wine-fuzzbunch/drive_c/fuzzbunch-debian/windows
wine cmd.exe
python fb.py
```
if someone wants to collaborate making a script to automatize everything, please do a pull request!

***

# How to Install
## Step 1: Install wine (Remember to be able to run wine32)
```
apt update
apt install wine winbind winetricks
```

Since fuzzbunch uses windows32 libraries, we are going to setup our own wine32 environment, also this will prevent to break any wine application that you are already using.

```
# Install wine32
dpkg --add-architecture i386 && apt-get update && apt-get install wine32

# Start a wine32 environment
WINEPREFIX="$HOME/.wine-fuzzbunch" WINEARCH=win32 wine wineboot

# Change WINEPREFIX for this session (modify your .bashrc accordingly if you want to make it permanent)
export WINEPREFIX=$HOME/.wine-fuzzbunch
```

## Step 2: Add python and fuzzbunch to PATH
```
wine regedit.exe
```
**Select:** HKEY_CURRENT_USER\Environment

**Right Click** Add String Value
```
Type: String
Name: PATH
Value: c:\\windows;c:\\windows\\system;C:\\Python26;C:\\fuzzbunch-debian\\windows\\fuzzbunch
```
![alt text](http://i.imgur.com/3HHUqBe.png)

## Step 3: Get files from GIT
```
cd $HOME/.wine-fuzzbunch/drive_c
git clone https://github.com/mdiazcl/fuzzbunch-debian.git
```

That will get you something like this:
```
fuzzbunch-debian/
├── installers
├── logs
└── windows
    ├── Bin
    ├── exploits
    ├── fuzzbunch
    ├── implants
    ├── lib
    ├── listeningposts
    ├── payloads
    ├── Resources
    ├── specials
    ├── storage
    └── touches
```

## Step 4: Install Python2.6 and pywin32 (winetrick will install both)
```
winetricks python26
```
> If you are having issues, Install each module (python-2.6 and pywin32-219.win32.py2.6) from the installer folder.

## Step 5: Run fuzzbunch
Switch to fuzzbunch folder

```
cd $HOME/.wine-fuzzbunch/drive_c/fuzzbunch-debian/windows
wine cmd.exe
```

That should get us **C:\fuzzbunch-debian\windows>** prompt. Run fuzzbunch (fb.py)

```
python fb.py
```

That's it, Fuzzbunch it's up and running!
Use it by your own responsability and for internal and authorized only purposes!
![alt text](http://i.imgur.com/2jA6qzT.png)

***
# FAQ
**Q: When I type on fuzzbunch it looks all screw-up. What's Going on? Did I do something wrong?**

**A:** FIXED by [@Alamot](https://github.com/Alamot), Thanks!
Make sure you have the HEAD version of this git. It was fixed at commit [@655eae5](https://github.com/mdiazcl/fuzzbunch-debian/commit/655ea5e421f233788ce8f64605971ca19f4e2b83).
