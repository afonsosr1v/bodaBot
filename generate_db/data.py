from tools import generate_random_string as rsg


USERS = [
    {
        "userID": rsg(20),
        "serverID": rsg(20),
        "username": "Nobrega",
        "password": "123",
        "email": rsg(20),
        "avatar": rsg(200),
    },
    {
        "userID": rsg(20),
        "serverID": rsg(20),
        "username": "Antunes",
        "password": "123",
        "email": rsg(20),
        "avatar": rsg(200),
    },
    {
        "userID": rsg(20),
        "serverID": rsg(20),
        "username": "Avô",
        "password": "123",
        "email": rsg(20),
        "avatar": rsg(200),
    },
]

ALBUMS = [
    {
        "albumID": rsg(20),
        "artist": "Unknown Mortal Orchestra",
        "album": "Multi Love",
        "albumImage": "https://images-ext-2.discordapp.net/external/SzkGJ7GQ__QRdSGLyY-5nmxxPbxOhiUwjHlJOCcjgGY/https/media.npr.org/assets/img/2015/05/12/umo_multilove_coverart_sq-3bafa12af3e061cde5a677cc75ccef9a8f5d4e52.jpg?width=468&height=468",
        "medianScore": "8",
    },
    {
        "albumID": rsg(20),
        "artist": "Kanye West",
        "album": "Jesus is King",
        "albumImage": "https://images-ext-1.discordapp.net/external/ARI6t9m8-OTRp8asRdcXy2Qz2i1lpL5r9_KBcho7TXM/https/media.pitchfork.com/photos/5db73da8fd8a1f0009ad5c80/master/pass/jesusisking_kanye.jpg?width=468&height=468",
        "medianScore": "1",
    },
    {
        "albumID": rsg(20),
        "artist": "Dillaz",
        "album": "Reflexo",
        "albumImage": "https://images-ext-1.discordapp.net/external/cEtW6wwX8sW4C8OPtOLKaJWZIdgDzGqw6GeE9zVgmpE/https/i.scdn.co/image/ab67616d0000b273972d7f11330a1b2eb3baf44f?width=468&height=468",
        "medianScore": "5",
    },
    {
        "albumID": rsg(20),
        "artist": "Daft Punk",
        "album": "Random Access Memories",
        "albumImage": "https://media.discordapp.net/attachments/1156691118549897256/1156693314318372875/Daft-Punk.png?ex=65397e98&is=65270998&hm=242789ab863fd2ab6e0b577e732230f163294142ee98cd2308fbfc494e2334fd&=&width=468&height=468",
        "medianScore": "10",
    },
]