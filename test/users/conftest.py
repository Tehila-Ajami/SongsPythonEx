import os

import pytest
import logging


@pytest.fixture(scope="session", autouse=True)
def step1():
    logger = logging.getLogger('my_log')
    fileh = logging.FileHandler('my_log', 'w')

    log = logging.getLogger()  # root logger
    for hdlr in log.handlers[:]:  # remove all old handlers
        log.removeHandler(hdlr)
    log.addHandler(fileh)  # set the new handler
