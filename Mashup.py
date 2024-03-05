import os
import sys
from pytube import Search
from pytube import YouTube
import moviepy.editor as mp
import glob


def downloadvideos(n, x):
    # Create a directory to store the videos
    if not os.path.exists("Videos"):
        os.mkdir("Videos")

    # Search for videos of the singer
    query = x + " music videos"
    s = Search(query)
    searchResults = {}
    i = 0
    for r in s.results:
        if i < n and r.length < 600:
            try:
                searchResults[r.title] = r.watch_url
                youtubeObject = YouTube(r.watch_url)
                youtubeObject = youtubeObject.streams.get_highest_resolution().download(
                    output_path='Videos', filename=f"video{i+1}.mp4")
                print(f"Downloaded video {i + 1}: {r.title}")
                i = i+1
            except:
                print("error occured")


def conversionAudio(duration, n):
    if not os.path.exists("Audios"):
        os.mkdir("Audios")

    for k in range(n):
        clip = mp.VideoFileClip(f"Videos/video{k+1}.mp4").subclip(0, duration)
        clip.audio.write_audiofile(f"Audios/audio{k+1}.mp3")


def Mashup(n, output):
    audio_clips = [mp.AudioFileClip(
        f"Audios/audio{i+1}.mp3") for i in range(0, n)]
    final_clip = mp.concatenate_audioclips(audio_clips)
    final_clip.write_audiofile(output)




if __name__ == "__main__":
    if (len(sys.argv) != 5):
        print("ERROR: Number of arguments are not correct")
        exit()

    downloadvideos(int(sys.argv[2]), sys.argv[1])
    conversionAudio(int(sys.argv[3]), int(sys.argv[2]))
    Mashup(int(sys.argv[2]), sys.argv[4])
