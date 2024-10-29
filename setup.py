from setuptools import setup, find_packages

setup(
    name="MHAQUEPipeline",
    version="0.1.0",
    description="ETLpipline",
    author="Mobasserul Haque",
    author_email="mh720@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        'console_scripts': [
            'etl_query=main:main',
        ],
    },
)