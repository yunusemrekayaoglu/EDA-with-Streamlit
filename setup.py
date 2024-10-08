from setuptools import setup, find_packages

setup(
    name='eda_stlit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas==2.0.3',
        'streamlit==1.21.0',
        'seaborn==0.12.2',
        'matplotlib==3.8.0'
    ],
    entry_points={
        'console_scripts': [
            'eda_stlit=app:main',
        ],
    },
    description='A Streamlit application for Exploratory Data Analysis',
    author='Yunus Emre KAYAOGLU',
    author_email='yunus.kayaoglu@hangikredi.com',
    url='https://github.com/yunusemrekayaoglu/eda_stlit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
