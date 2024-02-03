from setuptools import setup, find_packages

setup(
    name="sam-scraper",
    version="0.1.1",
    author="Diego Arrechea",
    author_email="diego.arrechea.job@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="https://github.com/Diego-Arrechea/sam-scraper",
    license="MIT",
    description="The `sam-scraper` is designed for seamless interaction with the sam.gov API,",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
)
