from setuptools import setup
from pathlib import Path

setup(
    name="markdown_strikethrough",
    version="0.0.1",
    url="https://github.com/BlTniki/markdown_strikethrough",
    description="A markdown python extension that enables you to create <s> tag by using ~~some text~~",
    author="BlTniki",
    author_email="shakarimovdima@ya.ru",
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    py_modules=['markdown_strikethrough'],
    install_requires=['markdown>=3.0'],
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
