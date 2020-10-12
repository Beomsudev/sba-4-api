import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()



setuptools.setup(
    name='bumsu_sba_api',
    version='1.0',
    description='Python Distribution Utilities',
    author='Greg Ward',
    author_email='bumsu1307@naver.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    )