__author__ = 'LesterTheTester'
from distutils.core import setup

setup(
    name="judy-bot",
    version="0.1",
    author="Bryan Lester, LesterTheTester, JudyTheJudgementalChicken",
    author_email="lester@bittorrent.com",
    packages=["judy"],
    url="https://github.com/LesterTheTester/judy",
    download_url="https://github.com/LesterTheTester/judy/tarball/0.1",
    license="LICENSE.txt",
    description="Judgemental Build-Reading Bot with Github Integration",
    long_description=open("README.txt").read(),
    keywords = ['build', 'failure analysis', 'judgemental', 'JudyTheJudgementalChicken', 'poultry'],
    install_requires=[
        "requests>=2.0.0"
    ],
    entry_points={
        'console_scripts': [
            'judy = judy.main:main',
        ]
    },
)