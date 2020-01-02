from unittest import TestCase

from url_extract import split_file


class Test(TestCase):
    def test_split_file(self):
        base, fullname = split_file('http://localhost:8000/plop/index.php?querywithparams=coucou')
        self.assertEqual('http://localhost:8000/plop', base)
        self.assertEqual('index.php', fullname)

