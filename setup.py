from setuptools import setup

setup(
    name="mcd",
    version="1.0.0",
    url="https://github.com/jasminsternkopf/mel_cepstral_distance",
    author="Jasmin Sternkopf",
    author_email="jasmin.sternkopf@mathematik.tu-chemnitz.de",
    packages=["mcd"],
    install_requires=[
        "appdirs>=1.4.4",
        "audioread>=2.1.9",
        "certifi>=2020.12.5",
        "cffi>=1.14.5",
        "chardet>=4.0.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "decorator>=4.4.2",
        "fastdtw>=0.3.4",
        "idna>=2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "joblib>=1.0.1; python_version >= '3.6'",
        "librosa",
        "llvmlite; python_version >= '3.6'",
        "numba; python_version >= '3.6' and python_version < '3.9'",
        "numpy",
        "packaging>=20.9; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pooch>=1.3.0; python_version >= '3.6'",
        "pycparser>=2.20; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pyparsing>=2.4.7; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2'",
        "requests>=2.25.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "resampy>=0.2.2",
        "scikit-learn>=0.24.1; python_version >= '3.6'",
        "scipy>=1.6.1",
        "six>=1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2'",
        "soundfile>=0.10.3.post1",
        "threadpoolctl>=2.1.0; python_version >= '3.5'",
        "urllib3>=1.26.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
    ],
    project_urls={
        "Bug Reports": "https://github.com/jasminsternkopf/mel_cepstral_distance/issues",
    },
)
