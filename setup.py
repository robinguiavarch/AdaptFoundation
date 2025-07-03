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
        # Core dependencies from NeuroSpin/Champollion
        'pandas',
        'scipy',
        'psutil',
        'matplotlib',
        'torch',
        'tqdm',
        'pqdm',
        'torchvision',
        'torch-summary',
        'tensorboard',
        'hydra-core',
        'hydra-joblib-launcher',
        'dataclasses',
        'OmegaConf',
        'scikit-learn',
        'scikit-image',
        'pytorch-lightning==2.1.3',
        'lightly',
        'plotly',
        'toolz',
        'ipykernel',
        'kaleido',
        'pytorch_ssim',
        'seaborn',
        'statsmodels',
        'umap-learn',
        'numpy',
        'wandb',
        'odfpy',
        'captum',
        
        # Foundation Models specific dependencies
        'timm>=0.6.0',                    # Transformers et ViTs
        'transformers>=4.20.0',           # HuggingFace models
        'open-clip-torch>=2.0.0',         # OpenCLIP implementations
        'clip-by-openai',                 # Original CLIP
        'dinov2',                         # DINOv2 if available via pip
        
        # Adaptation techniques
        'peft>=0.3.0',                    # Parameter Efficient Fine-Tuning (LoRA, Adapters)
        'loralib>=0.1.0',                 # LoRA implementation
        
        # Medical imaging (for MedSAM, MONAI)
        'nibabel',                        # Neuroimaging data 
        
        # Additional utilities
        'PyYAML>=5.3.0',
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