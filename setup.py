#!/usr/bin/env python
import os
import re
import sys
from pathlib import Path

from setuptools import find_packages
from setuptools import setup
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    """
    Distribution which almost always forces a binary package with platform name
    """

    def has_ext_modules(self):
        return super().has_ext_modules() or not os.environ.get('SETUPPY_ALLOW_PURE')


def read(*names, **kwargs):
    with Path(__file__).parent.joinpath(*names).open(encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


setup(
    name='signalfd',
    version='1.0.0',
    license='BSD-2-Clause',
    description='CFFI bindings for signalfd.',
    long_description='{}\n{}'.format(
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst')),
    ),
    author='Ionel Cristian Mărieș',
    author_email='contact@ionelmc.ro',
    url='https://github.com/ionelmc/python-signalfd',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[path.stem for path in Path('src').glob('*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # "Programming Language :: Python :: Implementation :: IronPython",
        # "Programming Language :: Python :: Implementation :: Jython",
        # "Programming Language :: Python :: Implementation :: Stackless",
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://python-signalfd.readthedocs.io/',
        'Changelog': 'https://python-signalfd.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/ionelmc/python-signalfd/issues',
    },
    keywords=[
        # eg: "keyword1", "keyword2", "keyword3",
    ],
    python_requires='>=3.9',
    install_requires=[
        'cffi>=1.0.0',
        # eg: "aspectlib==1.1.1", "six>=1.7",
    ],
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=='3.8'": ["backports.zoneinfo"],
    },
    # We only require CFFI when compiling.
    # pyproject.toml does not support requirements only for some build actions,
    # but we can do it in setup.py.
    setup_requires=(
        [
            'cffi>=1.0.0',
        ]
        if any(arg.startswith(('build', 'bdist')) for arg in sys.argv)
        else []
    ),
    cffi_modules=[f'{path}:ffi' for path in Path('src').glob('**/_*_build.py')],
)
