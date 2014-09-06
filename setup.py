__author__ = 'kinghadi'
import os

from setuptools import setup


def read(file_name):
    return open(os.path.dirname(__file__), file_name).read()


setup(
    name='pretty_print_dictionary',
    version=1.0,
    author='Hadi Sinaee, Sharif University of Technology',
    author_email='sinaee@ce.sharif.ir',
    description='A tool for showing dictionary objects in a more human-readable format.',
    license='GNU GPL',
    keywords='dict dictionary pretty print',
    url='https://github.com/kinghadi/Python-pretty_print_dictionary',
    packages=['pretty_print_dictionary'],
    long_description=read('README.md'),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta'

    ]
)