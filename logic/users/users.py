from infra.restUtils import *


def validate_user_after_add(user_name, response):
    ex_user = {
        "friends": [],
        "playlists": [],
        "user_name": user_name
    }
    ret_user = response.json().get("data")
    logging.info(f"add user {user_name} succeeded " + str(ex_user == ret_user))


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
    r = post_req(get_server_url()+"users/add_playlist", obj_playlist)
    return r
