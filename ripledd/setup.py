from setuptools import setup, find_packages

DESCRIPTION = "A nice and sweet API wrapper made for Ripledd"
LONG_DESCRIPTION = "A nice and sweet API wrapper made for Ripledd"


setup(
    name="ripledd",
    use_scm_version=True,
    author="Aditya Priyadarshi",
    author_email="adityapriyadarshi669@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["setuptools_scm", "requests"],
    keywords=["python", "API"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
