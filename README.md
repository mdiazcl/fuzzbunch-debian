# Kali/fuzzbunch-debian deployment guide
NSA/Fuzzbunch deployment for kali linux - Intructions. This version was designed to work under kali linux (to enhance our personal pentesting tools) using wine (32bits version) since Fuzzbunch uses python26 and WindowsXP. This is very usefull if you want to mix it with your Empire/Metasploit arsenal.

This particular version of Fuzzbunch has some personal fixes that I found over the internet:
 - Fuzzbunch.xml edited to be able to work on Wine
 - Fixed "listeningposts error" when running fb.py

**Contact Info**: miguel.diaz {at} mdiazlira.com | telegram @mdiazcl

## Original Work and special thanks
- **ShadowBroker:** https://github.com/misterch0c/shadowbroker.git
- **Knightmare2600 Unix Guide:** https://github.com/knightmare2600/ShadowBrokers
- **Sheila Berta Paper:** https://www.exploit-db.com/docs/41897.pdf

After you install everything you can use fuzzbunch using, if someone wants to collaborate making a script to automatize everything, please do a pull request!
```
cd ~/.wine/drive_c/fuzzbunch-debian/windows
wine cmd.exe
python fb.py
```

***

# How to Install
## Step 1: Install wine (Remember to be able to run wine32)
```
apt update
apt install wine winbind winetricks
```

## Step 2: Add python and fuzzbunch to PATH
```
wine regedit.exe
```
Select: HKey Current User\Environment (Right Click -> Add String Value)
```
Type: PATH
Value: c:\\windows;c:\\windows\\system;C:\\Python26;C:\\fuzzbunch-debian\\windows\\fuzzbunch
```
![alt text](http://i.imgur.com/3HHUqBe.png)

## Step 3: Get files from GIT
```
cd ~/.wine/drive_c
git clone https://github.com/mdiazcl/fuzzbunch-debian.git
```

That will get you something like this:
```
fuzzbunch-debian/
├── logs
└── windows
    ├── Bin
    ├── exploits
    ├── fuzzbunch
    ├── implants
    ├── lib
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

> :warning: You may have problems pressing the "Next" button. If that's the case you have to install wine32 by doing the following (it may take a while):

```
dpkg --add-architecture i386 && apt-get update && apt-get install wine32
```

## Step 5: Fuzzbunch Configure

Switch to our fuzzbunch working folder

```
cd ~/.wine/drive_c/fuzzbunch-debian/windows
wine cmd.exe
```

That should get us **C:\fuzzbunch-debian\windows>** prompt. Run fuzzbunch (fb.py)

```
python fb.py
```

That's it, Fuzzbunch it's up and running!
Use it by your own responsability and for internal and authorized only purposes!
![alt text](http://i.imgur.com/2jA6qzT.png)
