import os

import pytest
import logging


@pytest.fixture(scope="function", autouse=True)
def step1():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename='test.log', level=logging.INFO)
    logging.info("Start Test")
