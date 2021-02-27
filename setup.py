from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.main:main",
        ],
    },
    install_requires=[
        "psutil"
    ],
    version="0.1",
    author="Viachaslau Karpau",
    author_email="viachaslau_karpau@epam.com",
    description="Simple snapshooter",
    license="MIT",
)
