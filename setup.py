import os
from setuptools import setup, find_packages

setup(
    name='adaptfoundation',
    version='0.1.0',
    packages=find_packages(
        exclude=['tests*', 'notebooks*', 'experiments*']),
    license='CeCILL license version 2',
    description='Adaptation of Foundation Models '
                'for Cortical Folding Pattern Analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pandas',
        'numpy',  
        'torch',
        'torchvision', 
        'scikit-learn',
        'matplotlib',
        'PyYAML>=5.3.0',
        'tqdm',
        'timm>=0.6.0,<1.0',
        'transformers>=4.20.0,<5.0',
    ],
    extras_require={
        "anatomist": [
            'deep_folding @ git+https://git@github.com/neurospin/deep_folding'
        ]},
    python_requires='>=3.8',  # Plus récent que NeuroSpin pour compatibilité transformers
    url='https://github.com/robinguiavarch/AdaptFoundation',
    author='Robin Guiavarch',
    author_email='robin.guiavarch@telecom-paris.fr',
    maintainer='Pietro Gori',
    maintainer_email='pietro.gori@telecom-paris.fr',
)