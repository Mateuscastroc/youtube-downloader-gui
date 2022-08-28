from pytube import YouTube

print("Cole o link do video que deseja baixar:")
ytLinVideo = input()

ytVideo = YouTube(ytLinVideo)


print('Titulo do video:', ytVideo.title)
print('Autor do video:', ytVideo.author)

print("Para baixar somente o audio digite 1")
print("Para baixar o video digite 2")
optionDownload = int(input())



if optionDownload == 1:
    videoDownload = ytVideo.streams.get_audio_only()
    videoDownload.download('C:/Users/Mateus/Music')
else:
    videoDownload = ytVideo.streams.get_highest_resolution()    
    videoDownload.download('C:/Users/Mateus/Videos')



# def youtubeDownloader ():
#     print("Hello World")

# youtubeDownloader()