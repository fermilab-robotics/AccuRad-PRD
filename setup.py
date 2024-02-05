import setuptools 

long_description=open("README.md").read()

setuptools.setup(
    name="AccuRad-PRD",
    version="0.0.1",
    author="lpham",
    author_email="lpham@fnal.gov",
    description="AccuRad PRD USB Python Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fermilab-robotics/AccuRad-PRD",
    packages=['accurad'],
    install_requires=[
        'pyserial>=3.5',
    ],
    python_requires='>=3.7'
)