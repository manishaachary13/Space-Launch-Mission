from setuptools import setup, find_packages

setup(
    name='space_mission_launch_prediction',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    description='A PySpark-based regression model for predicting the cost of space mission launches using mission data.',
    author='R Manisha Achary',
    author_email='manisha.achary13@gmail.com',
    install_requires=[
        'pyspark==3.5.1',
        'pandas==2.2.1',
        'matplotlib==3.8.3',
        'numpy==1.26.4',
        'scikit-learn==1.4.1.post1',
        'seaborn==0.13.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
