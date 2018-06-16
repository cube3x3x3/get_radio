@echo off
setlocal
@echo %1
@echo %2

echo redio-url-start
SET NHK_R1_URL=https://nhkradioakr1-i.akamaihd.net/hls/live/511633/1-r1/1-r1-01.m3u8
SET NHK_R2_URL=https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8
SET NHK_FM_URL=https://nhkradioakfm-i.akamaihd.net/hls/live/512290/1-fm/1-fm-01.m3u8
SET OOSAKA_R1_URL=https://nhkradiobkr1-i.akamaihd.net/hls/live/512291/1-r1/1-r1-01.m3u8
SET OOSAKA_R2_URL=https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8
SET OOSAKA_FM_URL=https://nhkradiobkfm-i.akamaihd.net/hls/live/512070/1-fm/1-fm-01.m3u8

echo help-start
REM HELP
if "%2"=="" goto :HELP
if "%1"=="/?" (
    :HELP
    echo %0 [R1 or R2 or FM] [Recording Time]
    echo ex. %0 R2 900
    goto :EOF
)

echo if-start
REM ARGUMENT
SET RADIO=%1
if "%RADIO%"=="R1" (
    SET RADIO_URL=%NHK_R1_URL%
) else if "%RADIO%"=="R2" (
    SET RADIO_URL=%NHK_R2_URL%    
) else if "%RADIO%"=="FM" (
    SET RADIO_URL=%NHK_FM_URL%     
) else (
    SET RADIO_URL=%NHK_R2_URL%
)
if "0" lss "%2" (
    SET /A RECTIME=%2
    echo %RECTIME%
) else (
    SET /A RECTIME=900
)

echo date-start
REM DATE&TIME
SET LDATE=%DATE%
SET YR=%LDATE:~0,4%
SET MON=%LDATE:~5,2%
SET DAY=%LDATE:~8,2%
SET LTIME=%TIME: =0%
SET HR=%LTIME:~0,2%
SET MIN=%LTIME:~3,2%
SET SEC=%LTIME:~6,2%
SET TIMESTAMP=%YR%-%MON%%DAY%-%HR%%MIN%%SEC%
@echo %TIMESTAMP%

SET FILENAME=NHK-%RADIO%-%TIMESTAMP%

@echo %RADIO_URL%
@echo %RECTIME%
@echo %FILENAME%
SET TIMEOUT=10

ffmpeg -i %RADIO_URL% -t %RECTIME% -movflags faststart -c copy -bsf:a aac_adtstoasc %FILENAME%.m4a

:EOF
pause
