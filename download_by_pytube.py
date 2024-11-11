from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


def download_youtube(url):
    yt = YouTube(url)
    yt.streams.filter().get_by_resolution('480p').download(filename='oxxostudio_480p.mp4')


def get_desc(url):
    yt = YouTube(url, use_oauth=True)
    print(yt.streams.all())


if __name__ == '__main__':
    url = 'https://youtu.be/ioN2z8IQu8I'
    get_desc(url)
    # download_youtube(url)