import logging
import requests


def validate_response(response):
    if response.ok:
        logging.info(f"request url {response.url} succeed with status code {response.status_code}")
    else:
        logging.error(f"request failed with status code {response.status_code} failure reason {response.text}")


def get_server_url():
    return 'http://127.0.0.1:3002/'


def get_req(req_url, args):
    try:
        obj = requests.get(url=req_url, params=args)
        validate_response(obj)
        return obj
    except Exception as e:
        logging.error(f"exception error {e} while get url {req_url} ")


def post_req(req_url, body):
    try:
        obj = requests.post(url=req_url, json=body)
        validate_response(obj)
        return obj
    except requests.exceptions.RequestException as e:
        logging.error(f"exception error {e} while get url {req_url} ")


def put_req(req_url, body):
    try:
        obj = requests.put(url=req_url, json=body)
        validate_response(obj)
        return obj
    except requests.exceptions.RequestException as e:
        logging.error(f"exception error {e} while get url {req_url} ")
        return obj


def delete_req(req_url, args):
    try:
        obj = requests.delete(url=req_url, params=args)
        return obj
    except requests.exceptions.RequestException as e:
        logging.error(f"exception error {e} while delete {req_url} ")
