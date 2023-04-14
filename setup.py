from setuptools import setup
from neosekai_api.constants import VERSION
with open("README.md") as f:
    long_description = f.read()

setup(
    name="neosekai-api",
    version=VERSION,
    python_requires=">=3.10",
    install_requires=['lxml==4.9.2',
                      'beautifulsoup4>=4.11.2', 'requests==2.28.2'],
    author="John Erinjery",
    author_email="jancyvinod415@gmail.com",
    packages=['neosekai_api'],
    include_package_data=True,
    url="https://github.com/john-erinjery/neosekai-api/",
    license="MIT",
    description="An Unoffical Python API for neosekaitranslations.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Alpha",
        "Intended Audience :: Customer Service",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
