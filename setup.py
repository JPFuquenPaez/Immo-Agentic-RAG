from setuptools import setup, find_packages

setup(
    name="immo_rag",
    version="0.1",
    package_dir={"": "immo_rag"},
    packages=find_packages(where="immo_rag"),
    install_requires=[line.strip() for line in open("requirements.txt")],
    entry_points={
        'console_scripts': [
            'ingest=immo_rag.ingest:create_vector_store',
        ],
    },
)