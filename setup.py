from setuptools import setup, find_packages

setup(
    name='Zandi',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Algorithms for recursion and sorting arrays',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ZandiNkonzo/Zandi.git',
    author='Zandi Nkonzo',
    author_email='gill.macnkonzo@gmail.com'
)
