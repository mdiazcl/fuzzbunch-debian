# fuzzbunch-debian deployment guide
NSA/Fuzzbunch deployment for kali linux - Intructions.

This version of Fuzzbunch has some personal fixes like:
 - Edit Fuzzbunch.xml to be able to work on Wine
 - Fixed the listeningposts error when running fb.py

**Contact Info**: miguel.diaz {at} mdiazlira.com | :telegram: mdiazcl

# Original Work
- **ShadowBroker:** https://github.com/misterch0c/shadowbroker.git
- **Knightmare2600 Guide:** https://github.com/knightmare2600/ShadowBrokers
- **Sheila Berta Paper:** https://www.exploit-db.com/docs/41897.pdf

# How to Install
## Install wine (Remember to be able to run wine32)
```
apt update
apt install wine winbind winetricks
```

## Add python and fuzzbunch to PATH
```
wine regedit.exe
```
Select: HKey Current User\Environment (Right Click -> Add String Value)
```
Type: PATH
Value: c:\\windows;c:\\windows\\system;C:\\Python26;C:\\fuzzbunch-debian\\windows\\fuzzbunch
```

## Get files from GIT (I prepared this git for this tutorial)
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

## Install Python2.6 and pywin32 (winetrick will install both)
```
winetricks python26
```

:warning: **You may have problems pressing the "Next" button. If that's the case you have to install wine32 by doing the following (it may take a while):**

```
dpkg --add-architecture i386 && apt-get update && apt-get install wine32
```

## Fuzzbunch Configure
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
