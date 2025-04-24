from setuptools import setup, find_packages

setup(
    name='ec2_component',
    version='0.1.0',
    packages=find_packages(include=["ec2_component", "ec2_component.*"]),
    install_requires=[
        "pulumi>=3.0.0",
        "pulumi-aws>=5.0.0"
    ],
    python_requires='>=3.6',
)
