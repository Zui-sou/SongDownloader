from sclib import SoundcloudAPI, Playlist, Track

"""
https://soundcloud.com/threepool/thrax
https://soundcloud.com/djkipz/sets/lowin-for-pi
https://soundcloud.com/threepool/a-place-beneath?in=djkipz/sets/lowin-for-pi
"""


def download():
  link = str(input(f"Gib Link\n"))
  domain = str(link.lstrip("http" and "https").replace("://","").rsplit(".")[0])

  if domain == "soundcloud":
    api = SoundcloudAPI()
    typeOf = str(link.lstrip("http" and "https").replace("://","").replace(".com/","").replace("soundcloud","").split("/")[1])

    if typeOf == "sets":
      playlist = api.resolve(link)
      assert type(playlist) is Playlist
      for track in playlist.tracks:
        filename = f'./{track.artist} - {track.title}.mp3'
        with open(filename, 'wb+') as file:
          track.write_mp3_to(file)
        exit

    else:
      track = api.resolve(link)
      assert type(track) is Track
      filename = f'{track.artist} - {track.title}.mp3'
      with open (filename, 'wb+') as file:
        track.write_mp3_to(file)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

  elif domain == "youtube":
    print("youtube")
    return api

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

  elif domain == "open":
    print("spotify")
    return api


  else:
    print("Invalid Link Bozo")




download()