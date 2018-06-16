# https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8
# 1-r2-20171211T180234-01-770/707.ts
# URL = "https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-20171211T180234-01-770/707.ts"
# resp = requests.get(URL, timeout=1, headers=headers)
#URL = "https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/"

NHK_R1_URL="https://nhkradioakr1-i.akamaihd.net/hls/live/511633/1-r1/"
m3u8_R1="1-r1-01.m3u8"
NHK_R2_URL="https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/"
m3u8_R2="1-r2-01.m3u8"
NHK_FM_URL="https://nhkradioakfm-i.akamaihd.net/hls/live/512290/1-fm/"
m3u8_FM="1-fm-01.m3u8"

M3U_FOLDER = r"C:\\test_r\\m3u\\"
URL = NHK_FM_URL
m3u8_URL = URL+m3u8_FM
SLEEP_TIME = 60
TIMEOUT_TIME = 5
REC_TIME = 900
