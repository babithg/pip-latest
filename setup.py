from setuptools import setup, find_packages

setup(
    name='pip-latest',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'upgrade-pip=pip-latest.upgrader:main',
        ],
    },
    description='A package to upgrade pip to the latest version',
    author='Babith G',
    author_email='babithg@gmail.com',
    url='https://github.com/babithg/pip-latest',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
