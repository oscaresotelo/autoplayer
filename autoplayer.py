# import re, requests, subprocess, urllib.parse, urllib.request
# from bs4 import BeautifulSoup
# music_name = "Linkin Park Numb"
# query_string = urllib.parse.urlencode({"search_query": music_name})
# formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
# search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
# clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
# clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
# inspect = BeautifulSoup(clip.content, "html.parser")
# yt_title = inspect.find_all("meta", property="og:title")
# for concatMusic1 in yt_title:
#     pass
# print(concatMusic1['content'])
# subprocess.Popen(
# "start /b " + "vlc.exe " + clip2 + " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
# shell=True)
# # Alternatively, you can do this for simplicity sake:
# # subprocess.Popen("start /b " + "path\\to\\mpv.exe " + clip2 + "--no-video", shell=True)

import streamlit as st 
from pygame import mixer
import os 
mixer.init()
downloads_folder = "downloads"
mp3_files = [f for f in os.listdir(downloads_folder) if f.endswith(".mp3")]
st.write(mp3_files)

try:
    mixer.music.load(mp3_files)
except Exception:
    st.write("error no hay cancion")

if st.button("play"):
    mixer.music.play()

if st.button("stop"):
    mixer.music.stop()
if st.button("resume"):
    mixer.music.unpause()
