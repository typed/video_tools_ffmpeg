# video_tools_ffmpeg
基于ffmpeg的视频工具

剪辑命令：ffmpeg -ss 00:00:22 -t 00:05:12 -i Sekiro20230826182243.webm -vcodec copy -acodec copy output2.webm
合并命令：ffmpeg -f concat -i list.txt -c copy concat.mp4

防止2压：ffmpeg -i src.webm -c:v libx264 -vf zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p out.mp4

ffmpeg -ss 00:01:40 -t 00:00:10 -i "Sekiro™_ Shadows Die Twice_20231022213323.webm" -vcodec copy -acodec copy src.webm
ffmpeg -ss 00:01:40 -t 00:00:05 -i "Sekiro™_ Shadows Die Twice_20231022213323.webm" -c:v libx264 -vf zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,lutyuv="y=1.5*val",cas=0.7 out.mp4
ffmpeg -t 00:00:05 -i "Sekiro™_ Shadows Die Twice_20231016203714.webm" -c:v libx264 -vf scale=1920:1080,zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,eq=brightness=0.1:contrast=1.5,unsharp=5:5:2 -preset veryslow out2.mp4
ffmpeg -i src.webm -c:v libx264 -vf zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p -preset veryslow out.mp4