from setuptools import setup, find_packages

DESCRIPTION = "A nice and sweet API wrapper made for Ripledd"




setup(
    name="ripledd",
    version=1.2,
    author="Aditya Priyadarshi",
    author_email="adityapriyadarshi669@gmail.com",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["setuptools_scm", "requests"],"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
