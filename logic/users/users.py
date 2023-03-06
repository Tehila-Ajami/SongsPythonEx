import random

from infra.restUtils import *


def get_server_url():
    return 'http://127.0.0.1:3002/'


def get_rand_name():
    return "user_" + str(random.randint(1, 999))


def validate_user_after_add(user_name, response):
    ex_user = {
        "friends": [],
        "playlists": [],
        "user_name": user_name
    }
    ret_user = response.json().get("data")
    if ex_user == ret_user:
        logging.info(f"add user {user_name} succeeded")
    else:
        logging.error(f"add user {user_name} failed with response {response}")


def add_user(user_name, user_password):
    obj_user = {
        "user_name": user_name,
        "user_password": user_password
    }
    r = post_req(get_server_url() + "users/add_user", obj_user)
    logging.info(f"add_user response {r}")
    return r


def get_user(user_name):
    params = {"user_name": user_name}
    r = get_req(get_server_url() + "users/get_user", params)
    return r


def add_friend(friend_name, user_name, user_password):
    obj_friend = {
        "friend_name": friend_name,
        "user_name": user_name,
        "user_password": user_password
    }
    r = put_req(get_server_url() + "users/add_friend", obj_friend)
    return r


def add_playlist(playlist_name, user_name, user_password):
    obj_playlist = {
        "playlist_name": playlist_name,
        "user_name": user_name,
        "user_password": user_password
    }
    r = post_req(get_server_url() + "users/add_playlist", obj_playlist)
    return r
