import sys

from setuptools import find_packages, setup

cur_ver = sys.version_info[:2]
ver_str = ".".join(map(str, cur_ver))

if cur_ver < (3, 8) or cur_ver > (3, 10):
    raise RuntimeError(
        f"Python {ver_str} is unsupported. Please use a Python version between 3.8 and"
        " 3.10, inclusive."
    )

setup(
    name='omneer',
    version='v0.1.2',
    url='http://docs.omneer.xyz',
    license='MIT',
    author='William Blair',
    author_email='william.blair0708@gmail.com',
    description='Omneer SDK',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8,<3.11",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy>=1.19.0',
        'pandas>=1.2.0',
        'matplotlib>=3.3.0',
        'scipy>=1.6.0',
        'requests>=2.25.0',
        'beautifulsoup4>=4.9.0',
        'pytest>=6.0.0',
        'flake8>=3.9.0',
        'black>=21.6b0',
        'scikit-learn>=0.24.0',
        'torch>=1.9.0',
        'tqdm>=4.62.0',
        'xgboost>=1.4.0',
        'joblib>=1.0.0',
        'click>=8.0.1',
        'typer>=0.3.2',
        'halo>=0.0.31',
        'rich>=10.6.0',
        'seaborn>=0.11.0',
        'plotly>=5.1.0',
    ],
    entry_points={
        'console_scripts': [
            'omneer=omneer_cli.main:main',  # Replace with the correct module and function name
        ],
    },
        classifiers=[
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
    )