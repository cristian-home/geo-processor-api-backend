"""
Setup script for the geo-processor-api-backend package.
"""
from setuptools import setup, find_namespace_packages

setup(
    name="geo-processor-api-backend",
    version="0.1.0",
    packages=find_namespace_packages(include=["app", "app.*"]),
)
