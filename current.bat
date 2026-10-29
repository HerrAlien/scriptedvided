
set off=0.2
set d=F:\Videos\stock
set n1=Polaris_Family_RX570_barred
set n2=HD7790_PioneerGame_2026_08_03_22_33_36_325_zoomedOnAfterburner
set n3=GTX750Ti_DX11_PioneerGame_2026_08_04_19_51_21_016
set v1=%d%\%n1%.mp4
set v2=%d%\ArcRaidersMinusDX11Opt.mkv
set v3=%d%\%n3%.MP4
rem set v1=F:\Videos\Ryzen5_4600G\breel_R5_4600G_CpuAlone_barred.mp4
rem set v2=F:\Videos\stock\breel_R5_3600_6c12t.mp4

rem ffmpeg -loop 1 -i black.png -i %v1% -ss 13 -i %v2% -filter_complex "[1]crop=960:1080:0:0[cropped1];[2]crop=960:1080:0:0[cropped2];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=960:0[sbs];[sbs]drawtext=x=10:y=1000:box=1:boxborderw=10:boxcolor=white:font=Arial:fontsize=48:fontcolor=black:text='MSI A320M Grenade'[text1];[text1]drawtext=x=1620:y=1000:box=1:boxborderw=10:boxcolor=white:font=Arial:fontsize=48:fontcolor=black:text='GA-A320M-H'" -t 30 -c:v libx264 -preset medium -crf 17 side_by_side_1080.mp4

rem ffmpeg -loop 1 -i black.png -i %d%\%n1%.mp4 -i %d%\%n2%.mp4 -filter_complex "[1]crop=960:1080[cropped1];[2]crop=960:1080[cropped2];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=960:0" -t 29 -c:v libx264 -preset medium -crf 17 side_by_side_1080.mp4

rem ffmpeg -loop 1 -i hdreadygreen.png -i %v1% -ss 4 -i %v2% -filter_complex "[1]crop=640:720:0:0[cropped1];[2]crop=640:720:0:0[cropped2];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=640:0" -t 14 -c:v libx264 -preset medium -crf 17 %d%\side_by_side_720.mp4

rem ffmpeg -loop 1 -i hdreadygreen.png -ss 20 -i %v1% -ss 10 -i %v2% -ss 10 -i %v3% -filter_complex "[1]crop=426:720:0:0[cropped1];[2]crop=426:720:0:0[cropped2];[3]crop=428:720:0:0[cropped3];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=426:0[ov2];[ov2][cropped3]overlay=852:0" -t 30 -c:v libx264 -preset medium -crf 17 %d%\3_side_by_side_720.mp4

rem ffmpeg -loop 1 -i hdgreen.png -i %v1% -i %v2% -i %v3% -i %v4% -filter_complex "[1]scale=960:540[scaled1];[2]scale=960:540[scaled2];[3]scale=960:540[scaled3];[4]scale=960:540[scaled4];[0][scaled1] overlay=0:0[ov1];[ov1][scaled2] overlay=960:0[ov2];[ov2][scaled3] overlay=0:540[ov3];[ov3][scaled4] overlay=960:540" -t 20 merged.mp4 


rem ffmpeg -loop 1 -i black.png -i %v1% -i %v2% -filter_complex "[1]crop=960:1080[cropped1];[2]crop=960:864[cropped2];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=960:108" -t 30 -c:v libx264 -preset medium -crf 17 %d%\r5_5600_3600.mp4

rem ffmpeg -loop 1 -i black.png -i %v1% -i %v2% -filter_complex "[1]crop=960:1080[cropped1];[2]crop=960:1080[cropped2];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=960:0" -t 30 -c:v libx264 -preset medium -crf 17 1050Ti_both960s.mp4

rem ffmpeg -i %v1% -filter_complex "[0]rotate=-0.025[R0];[R0]scale='1920x1080:flags=lanczos'[S0];[S0]setsar=1" -c:v libx264 -preset medium -crf 17 %d%\%n1%_noTilt.mp4

rem ffmpeg -i %v1% -filter_complex "[0]rotate=-0.025[R0];[R0]crop=1280:720:0:300[cropped];[cropped]scale=1920:1080[s0];[s0]setsar=1" -c:v libx264 -preset medium -crf 17 %d%\%n1%_PcieX4.mp4

rem ffmpeg -ss 60 -i %v1% -filter_complex "[0]crop=640:360:0:0[cropped];[cropped]scale=1920:1080[s0];[s0]setsar=1" -c:v libx264 -preset medium -crf 17 %d%\%n1%_zoomedOnAfterburner.mp4

rem ffmpeg -i black.png -i %d%\%n1%.mp4 -filter_complex "[0][1]overlay=0:108" -c:v libx264 -preset medium -crf 18 %d%\%n1%_barred.mp4

rem ffmpeg -i %v1% -filter_complex "[0]crop=960:540:0:240[cropped];[cropped]scale='1920x1080:flags=lanczos'[S0];[S0]setsar=1" -c:v libx264 -preset medium -crf 18 %d%\%n1%_xeonOnly.mp4

rem ffmpeg -loop 1 -i black.png -i %v1% -i %v2% -filter_complex "[1]crop=1920:540:0:0[cropped1];[2]crop=1920:540:0:0[cropped2];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=0:540" -t 29 -c:v libx264 -preset medium -crf 17 %d%\TufX570Gaming+WiFi_tpm-rebar.mp4

rem ffmpeg -loop 1 -i hdreadygreen.png -i %v1% -ss 10 -i %v2% -filter_complex "[1]crop=640:720[cropped1];[2]scale='1600x900'[sc2];[sc2]setsar=1[ss2];[ss2]crop=640:720:900:180[cropped2];[0][cropped1]overlay=0:0[ov1];[ov1][cropped2]overlay=640:0" -t 30 -c:v libx264 -preset medium -crf 17 side_by_side_720.mp4


rem ffmpeg -i %v2% -filter_complex "[0]rotate=PI/2[rotated];[rotated]setsar=1/1" -c:v libx264 -preset medium -crf 17 %d%\broll_GTX1050Ti_outside_portrait.mp4


rem ffmpeg -i %v1% -filter_complex "[0]crop=720:405:0:0[cropped];[cropped]scale='1920x1080:flags=lanczos'[S0];[S0]setsar=1" -c:v libx264 -preset medium -crf 18 %d%\%n1%_quadrant2.mp4

rem ffmpeg -i %v1% -filter_complex "eq=brightness=0.075:gamma=1.1" -c:v libx264 -preset medium -crf 18 %d%\%n1%_brighter.mp4

ffmpeg -i %v1% -filter_complex "eq=brightness=0.045:gamma=1.025" -c:v libx264 -preset medium -crf 18 %d%\%n1%_slightlybrighter.mp4

rem ffmpeg -i black.png -i %v1% -filter_complex "[1:v]eq=brightness=0.05:gamma=1.1[eq1];[eq1]scale='1350x1080'[scaled];[0][scaled]overlay=285:0" -c:v libx264 -preset medium -crf 18 %d%\%n1%_barred.mp4

rem ffmpeg  -i black.png -i %v1% -filter_complex "[1:v]crop=1500:1080:90:0[cropped];[0][cropped]overlay=210:0" -c:v libx264 -preset medium -crf 18 %d%\%n1%_barred.mp4

rem ffmpeg  -i black.png -i F:\Videos\Aprils_Fool\case.jpg -i %v1% -i %v2% -filter_complex "[1]scale='720x560'[scaledImage];[2:v]crop=1200:1080[croppedCase];[3:v]scale='960x540'[scaledIO];[0][scaledIO]overlay=960:0[ov2];[ov2][croppedCase]overlay=0:0[ov1];[ov1][scaledImage]overlay=1200:540" -c:v libx264 -preset medium -crf 18 %d%\case.mp4

rem ffmpeg -i %v1% -filter_complex "crop=1280:720:640:360" -preset medium -crf 18 %d%\%n1%_zoomed.mp4

rem ffmpeg -i %v1% -filter_complex "eq=brightness=0.05:gamma=1.1" -c:v libx264 -preset medium -crf 18 %d%\%n1%_bright.mp4

rem ffmpeg -i %d%\%n1%.mkv -filter_complex "crop=1280:720:0:144" -c:v libx264 -preset medium -crf 18 %d%\%n1%_720p.mp4

rem ffmpeg -i %d%\%n1%.mp4 -i %d%\%n2%.mkv -filter_complex "[1]crop=640:1024:240:0[cropped];[0][cropped]overlay=1280:28" -t 30 -c:v libx264 -preset medium -crf 18 %d%\%n1%_QuadChannelOverlay.mp4