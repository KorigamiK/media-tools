from setuptools import setup

setup(
    name='media-tools',
    version='0.1.0',
    description='A tool to interact with streaming URLs easily',
    url='https://github.com/korigamik/media-tools',
    author='KorigamiK',
    author_email='korigamik@gmail.com',
    license='MIT',
    packages=['media_tools'],
    install_requires=['asyncio',
                      'aiohttp',
                      'aiofiles'
                      ],
    scripts=["bin/media-tools"],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
        'media manipulation',
        'media creation',
        'video downloader',
        'ffmpeg'
    ],
)
