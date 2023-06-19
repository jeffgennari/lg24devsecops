from setuptools import find_packages
from distutils.core import setup

setup(name='owmapi',
      version='0.1',
      description='OpenWeatherMap API Test for DevOps Exercise',
      install_requires=[
          'requests'
      ],
      classifiers=[
          'Programming Language :: Python :: 3.9'
      ],
      keywords=('OpenWeatherMap'),
      url='https://github.com/jwoytek/2022-devsecops-example',
      author='Jonathan Woytek',
      author_email='woytek@dryrose.com',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      long_description='OpenWeatherMap API Test for DevOps Exercise')

