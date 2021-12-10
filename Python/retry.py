#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
import sys
import time
from retrying import retry, RetryError
from requests.exceptions import HTTPError

logging.basicConfig(level=logging.INFO)

class TestRunner(object):
    @retry(stop_max_delay=10000)
    def get(self, url):
        logging.info(time.time())
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            raise response.raise_for_status()
        return response

if __name__ == "__main__":
    url = sys.argv[1]
    runner = TestRunner()
    try:
        response = runner.get(url)
        logging.info(response.headers)
    except HTTPError as e:
        logging.error(e)
    except RetryError as e:
        logging.error(e)
    except Exception as e:
        logging.critical(e)