import requests
import re
import json
from urllib.parse import urlparse

def get_bilibili_video(bv_id):
    # 1. 构造API请求
    api_url = f"https://www.bilibili.com/video/BV1DwFFerE4E/?spm_id_from=333.1007.tianma.1-1-1.click"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.bilibili.com/"
    }
    
    # 2. 获取视频信息
    response = requests.get(api_url, headers=headers)
    data = json.loads(response.text)
    video_title = data['data']['title']
    
    # 3. 提取视频下载链接
    video_url = data['data']['dash']['video'][0]['baseUrl']
    audio_url = data['data']['dash']['audio'][0]['baseUrl']
    
    # 4. 下载视频流
    video_content = requests.get(video_url, headers=headers).content
    audio_content = requests.get(audio_url, headers=headers).content
    
    # 5. 保存文件
    with open(f"{video_title}_video.mp4", "wb") as f:
        f.write(video_content)
        
    with open(f"{video_title}_audio.mp3", "wb") as f:
        f.write(audio_content)

# 使用示例（需要替换有效BV号）
get_bilibili_video("BV1uv411q7Mv")