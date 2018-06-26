import logging
import retry_requests
import bs4
import subprocess
import argparse
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('parse_nhkradio.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

parser = argparse.ArgumentParser(description='get nhk-gogaku streaming file')
parser.add_argument('kouza', metavar='kouza name', type=str, nargs='?', default='english/gendai', help='kouza is https://www2.nhk.or.jp/gogaku/ "english/business2" /')
args = parser.parse_args()
logger.info('args:%s', args.kouza)

# target_URL = "http://www.nhk.or.jp/gogaku/st/xml/english/gendai/listdataflv.xml"
prefix_target_URL ="http://www.nhk.or.jp/gogaku/st/xml/"
suffix_target = "/listdataflv.xml"
#_input = "english/gendai"
_input = args.kouza
target_URL = prefix_target_URL + _input + suffix_target
#m3u8_URL = "https://nhks-vh.akamaihd.net/i/gogaku-stream/mp4/18-ehs-4240-717.mp4/master.m3u8"
prefix_m3u8_URL = "https://nhks-vh.akamaihd.net/i/gogaku-stream/mp4/"
suffix_m3u8 = "/master.m3u8"

response = retry_requests.custom_session().get(target_URL, timeout=10)
contents = bs4.BeautifulSoup(response.content, "html.parser")
logger.debug('contents:%s', contents)
logger.debug('music:%s', contents.find_all("music"))

for music in contents.find_all("music"):
    logger.debug('music:%s', music.get('file'))
    uri = prefix_m3u8_URL+music.get('file')+suffix_m3u8
    logger.info('uri:%s', uri)
    filename = music.get('kouza')+music.get('nendo')+'-'+music.get('hdate') + '.m4a'
    logger.info('filename:%s', filename)
    ffmpeg_run = ('ffmpeg', '-i', uri, '-movflags', 'faststart', '-c', 'copy', '-bsf:a', 'aac_adtstoasc', filename, '-y')
    logger.debug('ffmpeg_run:%s', ffmpeg_run)
    subprocess.run(ffmpeg_run, shell=True, check=True)


exit()
