# Description: This script generates the database for the application.
# generate_db.py

from config import app, db
from models import User, Review
from rsg import generate_random_string as rsg

RREVIEWS_AND_USERS = [
    {
        "userID": rsg(20),
        "serverID": rsg(20),
        "reviews": [
            (rsg(20), "Unknown Mortal Orchestra", " Multi Love", "https://images-ext-2.discordapp.net/external/SzkGJ7GQ__QRdSGLyY-5nmxxPbxOhiUwjHlJOCcjgGY/https/media.npr.org/assets/img/2015/05/12/umo_multilove_coverart_sq-3bafa12af3e061cde5a677cc75ccef9a8f5d4e52.jpg?width=468&height=468", "6", "Percebo o hype do avô, é um bom album, mas não é de todo a minha cena, e não era o mood q eu estava a procura, bom album, pouco memoravel, muitas alturas lembrou-me de Thundercat xd"),
            (rsg(20), "Kanye West", "Jesus is King", "https://images-ext-1.discordapp.net/external/ARI6t9m8-OTRp8asRdcXy2Qz2i1lpL5r9_KBcho7TXM/https/media.pitchfork.com/photos/5db73da8fd8a1f0009ad5c80/master/pass/jesusisking_kanye.jpg?width=468&height=468", "5", "Fraquissimo, pior album do kanye, felizmente ja acabou, eu sei q falta o DONDA mas esse ouvi quando saiu e n me aptece ouvir again, Kanye vai lançar um album este ano, espero q se deixe de merdas catolicas e volte a ser mentalmente instavel"),
            (rsg(20), "My Chemical Romance", "The Black Parade", "https://images-ext-2.discordapp.net/external/6DC6m1FQgXfMvLX0w7fLRema98bJwRNiOuQxsL8Zau0/https/m.media-amazon.com/images/I/81fNQtNDw8L._UF1000%2C1000_QL80_.jpg?width=528&height=468", "10", "Melhor album dos MCR, emo essencial, unico motivo pelo qual o antunes começou a ouvir, temas incriveis guitarradas incriveis e bateria incrivel, pena n terem feito mais albuns deste calibre"),
        ],
    },
    {
        "userID": rsg(20),
        "serverID": rsg(20),
        "reviews": [
            (rsg(20), "Dillaz", "Reflexo", "https://images-ext-1.discordapp.net/external/cEtW6wwX8sW4C8OPtOLKaJWZIdgDzGqw6GeE9zVgmpE/https/i.scdn.co/image/ab67616d0000b273972d7f11330a1b2eb3baf44f?width=468&height=468", "8", "Este albúm representa tanto cultura, como dialeto, requinte, ternura e sobretudo sabedoria. Cada faixa é capaz de penetrar o meu encéfalo com tremenda facilidade, glorificando-me de conhecimento. Um simples obrigado ao André Chapelas."),
            (rsg(20), "Slipknot ", "The End, So Far", "https://images-ext-1.discordapp.net/external/W1Xi2OCea7BA_mZXqDvMwA4Y97FTve9r1u82oFshmiw/https/upload.wikimedia.org/wikipedia/en/8/8c/Slipknottheend.jpg", "10", "Fucking niggers, juro. Dar um 10/10 é sempre um tema sensível porém, aqui, justificável. Salazar em 1968 caiu da cadeira e a tristeza não podia ser maior. Tristeza pois os dois anos que seguiram não foram suficientes para este presenciar esta obra prima. É quase uma hora de constante masturbação auditiva, onde sou capaz de estimular-me à mais simples batida através da libertação do meu sémen. Foi o primeiro álbum que consumi desde do início ao fim com tremendo prazer no qual o único sofrimento foi imaginar que estava cada vez mais próximo de acabar. Não sou de todo capaz de tornar uma faixa, a dita faixa, porque estou constantemente a tentar não me vir ao ouvir isto em loop."),
        ],
    },
    {
        "userID": rsg(20),
        "serverID": rsg(20),
        "reviews": [
            (rsg(20), "Mastodon", "Crack The Skye", "https://images-ext-1.discordapp.net/external/XNXnSMMyZguSyJACGR7PkfeoGK3HXa8OcS91ZvcHvPs/https/upload.wikimedia.org/wikipedia/en/4/4a/Cracktheskye.jpg", "10", "Melhor album de sempre. Parece dorgas"),
            (rsg(20), "Daft Punk", "Random Access Memories", "https://media.discordapp.net/attachments/1156691118549897256/1156693314318372875/Daft-Punk.png?ex=65397e98&is=65270998&hm=242789ab863fd2ab6e0b577e732230f163294142ee98cd2308fbfc494e2334fd&=&width=468&height=468", "9", "É preciso ter paciência que todas a músicas precisam de cerca de 2 minutos para começar, mas depois disso passa para um dos melhores exemplos de jazz eletrónico sem limites. PS.: ignorar a get lucky"),
        ],
    }
]

with app.app_context(): # type: ignore
    db.drop_all()
    db.create_all()

    for user in RREVIEWS_AND_USERS:
        new_user = User(userID=user.get("userID"), serverID=user.get("serverID"))
        for reviews in user.get("reviews", []):
            new_user.reviews.append(
                Review(
                    reviewID=reviews[0],
                    artista=reviews[1],
                    album=reviews[2],
                    albumImage=reviews[3],
                    score=reviews[4],
                    review=reviews[5],
                )
            )
        db.session.add(new_user)
    db.session.commit()
        