from __future__ import with_statement
from setuptools import setup
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'src/onedrivesdk/version.txt'), encoding='utf-8') as f:
    version = f.read()


def main():
    package_list = ['onedrivesdk',
                    'onedrivesdk.request',
                    'onedrivesdk.model',
                    'onedrivesdk.extensions',
                    'onedrivesdk.helpers']

    if sys.version_info >= (3, 4):
        base_dir = 'python3'
        package_list.append('onedrivesdk.version_bridge')
    else:
        base_dir = 'python2'

    setup(
        name='onedrivesdk',

        version=version,

        description='Official Python OneDrive SDK for interfacing with OneDrive APIs',
        long_description=long_description,

        url='http://dev.onedrive.com',

        author='Microsoft',
        author_email='',

        license='MIT',

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.4',
            'Operating System :: OS Independent',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
        ],

        keywords='onedrive sdk microsoft',

        packages=package_list,

        package_dir={'onedrivesdk': 'src/onedrivesdk',
                     'onedrivesdk.request': 'src/' + base_dir + '/request'},

        package_data={'onedrivesdk': ['version.txt']},

        install_requires=['requests>=2.6.1'],

        extras_require={
            "samples": ["Pillow"],
            "tests": ["Mock"]
        },

        test_suite='testonedrivesdk'
    )

if __name__ == '__main__':
    main()
