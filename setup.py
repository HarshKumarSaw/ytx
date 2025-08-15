from setuptools import setup, find_packages

setup(
    name="ytx",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
    ],
    entry_points={
        "console_scripts": [
            "ytx=ytx.main:main"
        ]
    },
    author="Your Name",
    description="Interactive cross-platform YouTube downloader",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Video",
    ],
)