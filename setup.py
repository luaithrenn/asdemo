from setuptools import setup, find_packages

try:
    from pip._internal import main as pip_main
except:
    from pip import main as pip_main

pip_main(['install', '--upgrade', 'git+https://github.com/ibm-watson-iot/functions.git@'])

setup(
  name='demo',
  version='1.0',
  packages=find_packages(),
  dependency_links=['git+https:github.com/ibm-watson-iot/functions.git@']
  )
