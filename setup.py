from setuptools import setup, find_packages

setup(
    name='scrupe',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4==4.11.1',
        'certifi==2022.9.24',
        'charset-normalizer==2.1.1',
        'idna==3.4',
        'requests==2.28.1',
        'soupsieve==2.3.2.post1',
        'urllib3==1.26.12',
    ],
    entry_points={
        'console_scripts': [
            'scrupe = src.scrupe.scraper:run',
        ],
    },
)