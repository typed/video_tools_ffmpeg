# video_tools_ffmpeg
基于ffmpeg的视频工具

剪辑命令：ffmpeg -ss 00:00:22 -t 00:05:12 -i Sekiro20230826182243.webm -vcodec copy -acodec copy output2.webm
合并命令：ffmpeg -f concat -i list.txt -c copy concat.mp4