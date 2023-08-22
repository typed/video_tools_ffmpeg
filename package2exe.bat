pyinstaller -F -w ffmpeg2mp4.py
copy /y dist\ffmpeg2mp4.exe do.exe
rd /s /Q dist
rd /s /Q build
del ffmpeg2mp4.spec