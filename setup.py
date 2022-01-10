from setuptools import setup

setup(
    name='media-tools',
    version='0.1.0',
    description='A tool to interact with streaming URLs easily',
    url='https://github.com/korigamik/media-tools',
    author='KorigamiK',
    author_email='korigamik@gmail.com',
    license='MIT',
    packages=['media_tools', 'media_tools.utils'],
    install_requires=['asyncio',
                      'aiohttp',
                      'aiofiles'
                      ],
    scripts=["bin/media-tools"],
    keywords=['python', 'video', 'stream',
              'video stream', 'encode', 'ffmpeg'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
