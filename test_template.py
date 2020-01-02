from unittest import TestCase

from template import Template


class TestTemplate(TestCase):

    def test_variations(self):
        template = Template('test-template.txt')
        expected = ['myfile.php.bak', 'myfile.bak', 'myfile-bak.php']
        self.assertEqual(expected, template.variations('myfile.php'))

    def test_is_code(self):
        template = Template('test-template.txt')
        self.assertTrue(template.is_code('test{extension}'))
        self.assertTrue(template.is_code('test{filename}'))
        self.assertFalse(template.is_code('#test{extension}'))
        self.assertFalse(template.is_code(''))
        self.assertFalse(template.is_code('\r\n'))
        self.assertFalse(template.is_code('\r'))
        self.assertFalse(template.is_code('\n'))

    def test_variation(self):
        template = Template('template.txt')
        self.assertEqual('myfile.php.bak', template.variation('myfile', 'php', 'myfile.php', '{fullname}.bak'))
        self.assertEqual('myfile.bak', template.variation('myfile', 'php', 'myfile.php', '{filename}.bak'))
        self.assertEqual('myfile-bak.php', template.variation('myfile', 'php', 'myfile.php', '{filename}-bak.{extension}'))
