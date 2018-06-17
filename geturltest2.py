import requests
import m3u8
import time
import nhkstream_setting

# NHK_R2_URL="https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/"
# m3u8_R2="1-r2-01.m3u8"

M3U_FOLDER = nhkstream_setting.M3U_FOLDER
URL = nhkstream_setting.URL
m3u8_URL = nhkstream_setting.m3u8_URL
SLEEP_TIME = nhkstream_setting.SLEEP_TIME
TIMEOUT_TIME = nhkstream_setting.TIMEOUT_TIME
REC_TIME = nhkstream_setting.REC_TIME
START_TIME = time.time()
create_list = set()
print(M3U_FOLDER, m3u8_URL, URL, create_list)

def get_playlist(url, t=10):
    return m3u8.load(url, timeout=t)

def get_tsfiles(url, playlists, t=10):
    for tsfile in playlists:
        resp = requests.get(url+tsfile, timeout=t)
        filename = tsfile.split("/")[-1]
        create_list.add(filename)
        print(filename, create_list)
        f = open(M3U_FOLDER+filename, "wb")
        f.write(resp.content)
        f.close

def get_stream(start_time, rec_time):
    while (time.time() - start_time) < rec_time:
        playlist = get_playlist(m3u8_URL, TIMEOUT_TIME)
        # playlist.dump('output.m3u8')
        get_tsfiles(URL, playlist.files, TIMEOUT_TIME)
        time.sleep(SLEEP_TIME)

get_stream(START_TIME, REC_TIME)
print( sorted(create_list) )

with open(M3U_FOLDER+"test.m3u", "w", encoding="utf-8") as f:
    f.write("file ")
    f.write("\n file ".join(sorted(create_list)))



