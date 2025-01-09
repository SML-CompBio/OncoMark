with open('README.md', 'r') as f:
    long_description = f.read()

from setuptools import setup, find_packages

setup(
    name='OncoMark',
    version='1.0',    
    url='https://github.com/SML-CompBio/OncoMark',
    author='Shreyansh Priyadarshi',
    author_email='shreyansh.priyadarshi02@gmail.com',
    license='MIT License',
    packages=find_packages(),
    package_data={'OncoMark': ['hallmark_model.keras', 'hallmark_scaler.joblib', 'hallmark_feature.txt']},
    include_package_data=True,
    install_requires=['pandas==2.2.3',
                      'numpy==2.0.2',
                      'tensorflow==2.18.0',
                      'joblib==1.4.2',
                      'scipy==1.14.1'
                      ],
    description='A deep learning tool designed to predict Cancer Hallmark activities from tumor biopsy samples.',
    long_description=long_description,
    long_description_content_type='text/markdown',
)

