from setuptools import setup, find_packages

setup(
    name="train_notifier",
    version="0.1.0",
    author="Yifu Tian",
    author_email="yifutian@link.cuhk.edu.cn",
    description="A simple training notifier for TensorBoard loss monitoring and WeChat push",
    packages=find_packages(),
    install_requires=[
        "requests",
        "matplotlib",
        "Pillow",
        "tensorboard"
    ],
    python_requires='>=3.6',
)
