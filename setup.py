from setuptools import setup

setup(name='lemons',
      version='0.0.1',
      description='epic ml framework for the non-normies of ai.',
      author='Y0N1N1 (gabriel)',
      license='MIT',
      packages = ['lemons'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['math','os'],
      python_requires='>=3.8',
      extras_require={
        'dev': [
            "math",
            "os"
        ],
      },
      include_package_data=True)
