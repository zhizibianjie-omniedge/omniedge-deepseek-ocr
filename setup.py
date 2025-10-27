#!/usr/bin/env python3
"""
omniedge-deepseek-OCR 安装配置

简单易用的DeepSeek-OCR文字识别模块
作者: 智子边界(OmniEdge)
"""

from setuptools import setup, find_packages
import os

# 读取README文件
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "omniedge-deepseek-OCR 简单易用的OCR识别模块"

# 读取requirements文件
try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    requirements = ["requests>=2.25.0", "Pillow>=8.0.0"]

setup(
    name="omniedge-deepseek-ocr",
    version="1.0.0",
    author="智子边界(OmniEdge)",
    author_email="contact@omniedge.com",
    description="简单易用的DeepSeek-OCR文字识别模块",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr",
    project_urls={
        "Bug Reports": "https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr/issues",
        "Source": "https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr",
        "Documentation": "https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr#readme",
        "Gitee": "https://gitee.com/omniedge/omniedge-deepseek-ocr",
    },
    py_modules=["deepseek_ocr", "config"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "omniedge-ocr=deepseek_ocr:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md"],
    },
    keywords=[
        "ocr", "deepseek", "image-recognition", "text-extraction",
        "chinese-ocr", "文字识别", "图像识别", "智子边界", "omniedge"
    ],
    license="MIT",
    platforms=["any"],
    zip_safe=False,
)