# unlock
ytdl fork with additional features

<p align="center">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/downloads/sourabhkv/ytdl/total?logo=GitHub"></a>
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/downloads/sourabhkv/ytdl/latest/total?logo=github"> <a href="https://github.com/sourabhkv/ytdl/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/sourabhkv/ytdl"></a>
<a href="https://www.youtube.com/channel/UCdr0BYy90kbqE2AN4GU2-oQ/featured"><img alt="YouTube Channel Views" src="https://img.shields.io/youtube/channel/views/UCdr0BYy90kbqE2AN4GU2-oQ?style=social"></a>
<a href="https://github.com/sourabhkv/ytdl/commits"><img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/sourabhkv/ytdl?color=red&label=Commit" ></a> <a href="https://python.org"><img alt="python" src="https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54" ></a> <a href="https://python.org"><img alt="python" src="https://img.shields.io/badge/c%23-%23239120.svg?style=flat&logo=c-sharp&logoColor=white" ></a> <img alt="Windows" src="https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white" ></a>
</p>
<p align="center">
<a href="https://python.org"><img alt="python" src="https://user-images.githubusercontent.com/55890376/187068580-eabf12eb-cfce-49cb-a026-664087963ffe.png" ></a>
<br>
<a href="https://github.com/sourabhkv/ytdl#support-us"><img alt="python" src="https://img.shields.io/badge/Phonepe-54039A?style=for-the-badge&logo=phonepe&logoColor=white" ></a>
<a href="https://www.paypal.com/paypalme/PinakiSahu"><img alt="python" src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" ></a>
</p>
<p align="center">
<a href="https://t.me/ytdlgui"><img alt="GitHub release (latest by date)" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
</p>
<p align="center">
<a href="https://sourabhkv.github.io/ytdl/"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/sourabhkv/ytdl?color=violet&label=Download%20latest&logo=windows&logoColor=%230574FF&style=for-the-badge"></a>
</p>

A GUI program that runs on top of yt-dlp and ffmpeg to download videos and audio. **This project is only for educational purpose DO NOT SELL . DO NOT 
plagiarize. USE AT YOUR RISK . I DO NOT PROMOTE ANY ILLEGAL DOWNLOADS .**<br>

　　　　　　　　　　　　　　　　　　　　![python](https://user-images.githubusercontent.com/55890376/208916421-d983d873-8dd8-4d53-949a-16959f9f6df9.png)&nbsp;&nbsp;&nbsp;&nbsp;
![yt-dlp](https://user-images.githubusercontent.com/55890376/208916592-4cfc3036-6b0b-4ccf-9fa7-5214c9440bc5.png)&nbsp;&nbsp;&nbsp;&nbsp;
![ffmpeg](https://user-images.githubusercontent.com/55890376/208916616-76aace34-17e9-4865-b73c-bd1777b416bc.png)&nbsp;&nbsp;&nbsp;&nbsp;
![ps](https://user-images.githubusercontent.com/55890376/208916682-7d245f1a-1881-42dc-b56c-b3ff8fe11939.png)&nbsp;&nbsp;&nbsp;&nbsp;

**Version 23.xx.yy coming soon....**<br>
Update model 3 will built using python 3.8.10 <br>
Windows 7 support will be dropped in Oct 2024.<br>
~~⚠️ ALERT CURRENTLY SUPPORTED VERSIONS WILL NO LONGER RECEIVE UPDATES ,YTDL WILL USE **PYTHON 3.10.7** with latest libraries<br>
**⚠️ Windows 7 version will be released separately which will be based on python 3.8.10**<br>~~



[yt-dlp](https://github.com/yt-dlp/yt-dlp) and [youtube-dl](https://github.com/ytdl-org/youtube-dl) licensed under [The Unlicense](https://unlicense.org/)<br>
[FFmpeg](https://ffmpeg.org/) is licensed under the [GNU Lesser General Public License (LGPL)](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) version 2.1 or later.<br>
[AtomicParsley](https://github.com/wez/atomicparsley) is licensed under [GPL-2.0 license](https://github.com/wez/atomicparsley/blob/master/COPYING)<br>
[pygame](https://www.pygame.org/news) is licensed under  [GNU LGPL version 2.1](https://www.gnu.org/copyleft/lesser.html)

## Ytdl unlocked (Pro)
Expanded supported websites<br>
made with python 3.8 and 3.10<br>
multi video supports que<br>
multi video supports more URLs other than youtube.com<br>
Hyper user<br>
Wav format for playlist and more.<br>

## Building executable
### Windows

---

1. Clone this repository
2. Install the following dependencies
```
python >= 3.8.10
ffmpeg >= 3.3.4
yt-dlp latest version
```
- ffmpeg and yt-dlp should be placed in cloned dir
Libraries
```
pyinstaller==5.6.2
Pillow==9.4.0
yt-dlp==2023.1.6
virtualenv==20.17.1
pycryptodomex==3.16.0
requests==2.28.1
psutil==5.9.4
pytube==12.1.2
```
3. Run the [builder.ps1](https://github.com/sourabhkv/ytdl/blob/main/builder.ps1)
4. Build will be generated `./dist/Youtube-dl GUI/` folder

### Linux (Still in preview)

---

1. Follow step 1 and 2 as above
2. Give permission to builder.sh
```
chmod +x builder.sh
```
- Before compiling change few lines in code which ask for logo.ico
3. Run the builder.sh
```
./builder.sh
```
4. Build will be generated `./dist/Youtube-dl GUI/` folder

## CONTRIBUTING
### Opening an issue
Bugs and suggestions should be reported at: [/ytdl/issues](https://github.com/sourabhkv/ytdl/issues)
Select the type of issue
- `Bug report`
- `Feature request`
- `Ask a question`

Please see the issues section before opening issue<br>
Duplicate issues will not be entertained and make sure you are on latest version<br>
Adding Screenshots/videos will be helpful.<br>

### Creating Pull request
Do not include database files, other dependencies in PR.<br>

## Support Us
If you have liked my work and want to support please consider donating.<br>
Help to keep Ytdl active and running by donating. It will be really helpful and appreciated if you donate or contribute to us. Any amount is appreciated.<br><br>
<a href="https://github.com/sourabhkv/ytdl#support-us"><img alt="python" src="https://img.shields.io/badge/Phonepe-54039A?style=flat&logo=phonepe&logoColor=white" ></a>
: `sourabhkv@upi`
<br><br>
<a href="https://www.paypal.com/paypalme/PinakiSahu"><img alt="python" src="https://img.shields.io/badge/PayPal-00457C?style=flat&logo=paypal&logoColor=white" ></a>
:[`PinakiSahu`](https://www.paypal.com/paypalme/PinakiSahu)
<p align="center">
<img alt="GitHub release (latest by date)" src="https://user-images.githubusercontent.com/55890376/190670832-71eda095-3b87-4d9a-b7cb-1433ed2f4fe5.png">





**Want Early build access?**<br>
<br><a href="https://t.me/ytdlgui"><img alt="GitHub release (latest by date)" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a><br>
</p>

## Useful Links
[Supported Websites youtube-dl](http://ytdl-org.github.io/youtube-dl/supportedsites.html)<br>
[Supported websites yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)<br>
[youtube-dl](https://github.com/ytdl-org/youtube-dl)<br>
[yt-dlp](https://github.com/yt-dlp/yt-dlp)<br>
[Pytube](https://pytube.io/en/latest/)<br>
[ffmpeg](https://ffmpeg.org/ffmpeg.html)<br>
[AtomicParsley](http://atomicparsley.sourceforge.net/)<br>
[Pygame](https://www.pygame.org/wiki/about)<br>
[Inno Setup](https://jrsoftware.org/isinfo.php)<br>