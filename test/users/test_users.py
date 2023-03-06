import logging
import random
import pytest
from logic.users.users import *


def get_add_user(user_name, user_password):
    logging.info(f"step1 - add user user name {user_name} user password {user_password}")
    add_user(user_name, user_password)
    logging.info(f"step2 - get user {user_name} ")
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
    logging.info(f"step3 - add same user name {user_name} second")
    res = add_user(user_name, user_password)
    duplicate_error = str(f"user with name {user_name} already exists" in str(res.content))
    logging.info("validate add duplicate user name return error succeeded " + duplicate_error + " " + str(res.content))


@pytest.mark.test_2
def test_add_some_users(step1):
    for i in range(1, 3):
        user_name = f"user_{i}"
        user_password = f"pass_{i}"
        get_add_user(user_name, user_password)


@pytest.mark.test_3
def test_add_not_exists_friend(step1):
    user_name = "main user name"
    user_password = "main user pass"
    # get_add_user(user_name, user_password)
    logging.info(f"step3 - add un exists user name as friend to user {user_name}")
    res = add_friend("blala", user_name, user_password)
    not_exists_user_error = str(f"the user {user_name} does not exist" in str(res.content))
    logging.info("validate add not exists user as friend return error succeeded " + not_exists_user_error + " " + str(
        res.content))


@pytest.mark.test_4
def test_add_friend(step1):
    # step 1 Add main user
    user_name = "main user name " + str(random.randint(1, 999))
    user_password = "main user pass"
    get_add_user(user_name, user_password)
    # step 2 Add another user
    f_user_name = "friend user name" + str(random.randint(1, 999))
    f_user_password = "friend user pass"
    get_add_user(f_user_name, f_user_password)
    logging.info(f"step4 - add exists user name {f_user_name} as friend to user {user_name}")
    add_friend(f_user_name, user_name, user_password)
    logging.info(f"step4 - get exists user {f_user_name} details")
    res_get_user = get_user(user_name)
    user_friend_list = res_get_user.json().get("data").get("friends")
    logging.info("validate add user as friend succeeded " + f_user_name in
                 user_friend_list + f"user {user_name} friends list")
    logging.info(' '.join(user_friend_list))
