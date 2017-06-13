from setuptools import setup, find_packages

setup(
    name='earning_spider',
    version="0.1",
    packages=find_packages(),
    scripts=['run.py'],
    install_requires=['scrapy',
                      'sqlalchemy'
                      ],
    author="Andy.Xu",
    author_email="xu9529@gmail.com",
    description="nasdaq earning spider",
    license="MIT",
)
