class MP3:
    def __init__(self, path):
        self.path = path

    def play(self):
        print("MP3 çalıyor")

class WAV:
    def __init__(self, path):
        self.path = path

    def play(self):
        print("WAV çalıyor")

class WMA:
    def __init__(self, path):
        self.path = path

    def play(self):
        print("WMA çalıyor")

class M4A:
    def __init__(self, path):
        self.path = path

    def play(self):
        print("M4A çalıyor")

def playMusic(p):
    p.play()

#mp3 = MP3('c:\\temp\\x.mp3')
#wav = WAV('c:\\temp\\y.wav')
#wma = WMA('c:\\temp\\z.wma')
#m4a = M4A('c:\\temp\\k.m4a')
#GNU/Linux'a göre düzenlenecektir.

mp3 = MP3('/home/hwpplayer1/Music/x.mp3')
wav = WAV('/home/hwpplayer1/Music/y.wav')
wma = WMA('/home/hwpplayer1/Music/z.wma')
m4a = M4A('/home/hwpplayer1/Music/k.m4a')

playMusic(mp3)
playMusic(wav)
playMusic(wma)
playMusic(m4a)