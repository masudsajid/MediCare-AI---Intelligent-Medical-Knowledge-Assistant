#!/usr/bin/env python3
"""
Setup script for Medical RAG Chatbot
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="medical-rag-chatbot",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Medical Research Chatbot using LLM and Pinecone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/Medical-RAG-Chatbot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "": ["*.html", "*.css", "*.pdf"],
    },
)