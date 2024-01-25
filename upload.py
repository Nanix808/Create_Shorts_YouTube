import os
from tiktok_uploader.upload import upload_videos
from tiktok_uploader.auth import AuthBackend


# single video
# upload_video('video.mp4',
#             description='this is my description',
#             cookies='cookies.txt')

videos = []
# Указываем путь к директории
DIRECTORY = "download/"

# Получаем список файлов
files = os.listdir(DIRECTORY)

for file in files:
    if file.endswith(".mp4"):
        videos.append({"path": os.path.join(DIRECTORY, file), "title": file[:-5]})


auth = AuthBackend(cookies="cookies.txt")
upload_videos(videos=videos, auth=auth)


# вопросы #ответы #question #answer

# import requests
# import json

# url = "https://open.tiktokapis.com/v2/post/publish/inbox/video/init/"
# headers = {
#     'Authorization': 'Bearer {$UserAccessToken}',
#     'Content-Type': 'application/json; charset=UTF-8'
# }
# data = {
#     "source_info": {
#         "source": "FILE_UPLOAD",
#         "video_size": exampleVideoSize,
#         "chunk_size" : exampleChunkSize,
#         "total_chunk_count": exampleTotalChunkCount
#     }
# }
# response = requests.post(url, headers=headers, data=json.dumps(data))
