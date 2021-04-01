import pafy

song_url = input('Enter song url:')
v = pafy.new(song_url)
print(v.title)
s = v.getbestaudio()
filename = s.download()
print("Size is %s" % s.get_filesize())
mp4_dir = print('{}.mp4'.format(v.title))