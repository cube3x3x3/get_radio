import logging
import unittest
import requests
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def custom_session(
    retries=5,
    backoff_factor=0.5,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = requests.packages.urllib3.util.retry.Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = requests.adapters.HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

class TestRequestsMethods(unittest.TestCase):
    def test_retry(self):
        logger.info('start test_retry')
        with self.assertRaises(requests.exceptions.ConnectionError) as x:
            response = custom_session(2, 0.2).get(
                'http://localhost:9999',
            )
        logger.info('test_retry %s', x.exception)
        logger.info('end test_retry')

    def test_timeout(self):
        logger.info('start test_timeout2')
        with self.assertRaises(requests.exceptions.Timeout) as x:
            response = custom_session(2, 0.2).get(
                'http://httpbin.org/delay/10',
                timeout=0.001
            )
        logger.info('test_timeout2 %s', x.exception)
        logger.info('end test_timeout2')


    def test_status500(self):
        logger.info('start test_status')
        with self.assertRaises(requests.exceptions.RetryError) as x:
                response = custom_session(2, 0.2).get(
                    'http://httpbin.org/status/500',
                )
        logger.info('test_status500 %s', x.exception)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main(verbosity=2)


