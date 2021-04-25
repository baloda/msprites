import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="msprites",
    version="1.0.6",
    author="Dharmveer Baloda",
    author_email="dharmvrbaloda836@gmail.com",
    description="Create thumbnail spritesheet from mp4 media files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baloda/msprites",
    project_urls={
        "Bug Tracker": "https://github.com/baloda/msprites/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)