from setuptools import setup

setup(
    name='xkcd_frame',
    version='1.0.0',
    description='Software for a digital frame displaying XKCD comics',
    py_modules=['xkcd_frame'],
    install_requires=[
        'xkcd-dl',
        'flask',
        ]
    )

