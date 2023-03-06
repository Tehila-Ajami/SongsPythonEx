from infra.restUtils import *


def add_song(song_genre, song_performer, song_title, song_year):
    obj_song = {
        "song_genre": song_genre,
        "song_performer": song_performer,
        "song_title": song_title,
        "song_year": song_year
    }
    r = post_req(get_server_url() + "songs/add_songs", obj_song)
    logging.info(f"add_song response {r}")
    return r


def get_song(song_title):
    params = {"song_title": song_title}
    r = get_req(get_server_url() + "users/get_user", params)
    return r