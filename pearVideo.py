import requests

# https://video.pearvideo.com/mp4/short/20240629/cont-1795028-71107205-hd.mp4
# https://video.pearvideo.com/mp4/short/20240629/1720150767824-71107205-hd.mp4
url="https://www.pearvideo.com/video_1795028"
contId=url.split('_')[1]
videoRealUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.4717254094579104"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'Referer': 'https://www.pearvideo.com/video_1795028'
}
response = requests.get(videoRealUrl, headers=header)
dict = response.json()
srcUrl=dict['videoInfo']['videos']['srcUrl']
systemTime=dict['systemTime']
srcUrl=srcUrl.replace(systemTime, "cont-"+contId)
print(srcUrl)
with open("test.mp4", "wb") as f:
    f.write(requests.get(srcUrl, headers=header).content)
