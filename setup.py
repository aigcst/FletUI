'''
Description : 
Author      : aigcst
Copyright   : CSTOS
Date        : 2025-06-13 22:11:06
LastEditors : aigcst
LastEditTime: 2025-06-14 22:02:22
Modified    : 
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fletui",                  # 包名称
    version="0.0.1",                                   # 包版本
    author="aigcst",                           # 作者
    license='MIT',                                     # 协议简写
    author_email="aigcst@outlook.com",                 # 作者邮箱
    description="A UI package based on Flet for more convenient construction of interface programs.",             # 工具包简单描述
    long_description=long_description,                 # readme 部分
    long_description_content_type="text/markdown",     # readme 文件类型
    install_requires=[                                 # 工具包的依赖包
    'flet>=0.28.3',
    ],
    url="https://github.com/aigcst/FletUI",       # 包的开源链接
    packages=setuptools.find_packages(),               # 不用动，会自动发现
    classifiers=[                                      # 给出了指数和点子你的包一些额外的元数据
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
