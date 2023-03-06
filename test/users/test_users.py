import logging
import random
import pytest
from logic.users.users import *


def get_add_user(user_name, user_password):
    logging.info(f"add user user name {user_name} user password {user_password}")
    add_user(user_name, user_password)
    logging.info(f"get user {user_name} ")
    get_user_res = get_user(user_name)
    logging.info(
        f"Get user name {user_name} after add user succeeded"
        f" {get_user_res.ok} get user response {get_user_res.content}")
    validate_user_after_add(user_name, get_user_res)


@pytest.mark.test_1
def test_duplicate_user(step1):
    user_name = "tehila2"
    user_password = "pass2"
    user1 = {"user_name": user_name,
             "user_password": user_password
             }
    # step1
    get_add_user(user_name, user_password)
    logging.info(f"add same user name {user_name} second")
    res = add_user(user_name, user_password)
    duplicate_error_str = "user with name {user_name} already exists"
    is_error_duplicate_user = duplicate_error_str in res.content
    if is_error_duplicate_user:
        logging.info("validate add duplicate user name return error succeeded")
    else:
        logging.error("validate add duplicate user name return error failed error not as expected " +
                      res.content)


@pytest.mark.test_2
def test_add_some_users(step1):
    for i in range(1, 3):
        user_name = f"user_{i}"
        user_password = f"pass_{i}"
        get_add_user(user_name, user_password)


@pytest.mark.test_3
def test_add_not_exists_friend(step1):
    user_name = get_rand_name()
    user_password = "main user pass"
    get_add_user(user_name, user_password)
    logging.info(f"step3 - add not exists user name as friend to user {user_name}")
    res = add_friend("blala", user_name, user_password)
    not_exists_user_error = str(f"the user {user_name} does not exist" in str(res.content))
    if not_exists_user_error:
        logging.info("validate add not exists user as friend return error succeeded " + str(res.content))
    else:
        logging.error("validate add not exists user as friend return error failed " + str(res.content))


@pytest.mark.test_4
def test_add_friend(step1):
    # step 1 Add main user
    user_name = get_rand_name()
    user_password = "main user pass"
    get_add_user(user_name, user_password)
    # step 2 Add another user
    f_user_name = get_rand_name()
    f_user_password = "friend user pass"
    get_add_user(f_user_name, f_user_password)
    logging.info(f"step 3 - add exists user name {f_user_name} as friend to user {user_name}")
    add_friend(f_user_name, user_name, user_password)
    logging.info(f"step 4 - get exists user {f_user_name} details")
    res_get_user = get_user(user_name)
    user_friend_list = res_get_user.json()["data"]["friends"]
    is_friend_added = f_user_name in user_friend_list
    if is_friend_added:
        logging.info(f"step 5 -validate add friend {f_user_name} as friend to user {user_name} friends list")
    else:
        logging.error(f"step 6 -failed add friend {f_user_name} as friend to user {user_name} friends list")
    logging.info(' '.join(user_friend_list))
