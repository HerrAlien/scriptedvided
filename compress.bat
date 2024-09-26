@echo off
call %~dp0setenv.bat
set INPUTFILE=%1
ffmpeg -y -i %1 -c:a libvorbis -qscale:a 9 -c:v libx264 -preset slow -crf 16 %INPUTFILE:~0,-4%_compressed.mp4
