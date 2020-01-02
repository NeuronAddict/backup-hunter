from types import SimpleNamespace
from unittest import TestCase

from backuphunter.search import search


class TestScript(TestCase):

    def test_url(self):
        expected = ['http://localhost:8000/index-bak.php', 'http://localhost:8000/index.php~']
        args = SimpleNamespace(url='http://localhost:8000/index.php', template=False, verbose=False, proxy=False,
                               cookie=False, urls_file=False)
        self.assertEqual(expected, search(args))

    def test_urlfile(self):
        expected = ['http://localhost:8000/index-bak.php', 'http://localhost:8000/index.php~']
        args = SimpleNamespace(url=False, template=False, verbose=False, proxy=False,
                               cookie=False, urls_file='urls.txt')
        self.assertEqual(expected, search(args))
