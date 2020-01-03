from setuptools import setup

setup(name='backup-hunter',
      version='0.1',
      description='Find backup files in web server',
      url='http://github.com/neuronaddict/backup-hunter',
      author='neuronaddict',
      author_email='',
      license='Apache 2.0',
      packages=['backuphunter'],
      package_data={'backuphunter': ['template.txt']},
      zip_safe=False, install_requires=['requests', 'argparse', 'termcolor'])
