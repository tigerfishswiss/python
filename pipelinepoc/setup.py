import setuptools

setuptools.setup(
    name="pipelinepoc_tigerfish",
    version="0.0.1",
    author="Tigerfish",
    author_email="tigerfish.download@gmail.com",
    description="A small example package",
    long_description="long_description",
    long_description_content_type="text/markdown",
    

    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    
    install_requires=[
             'docutils',
             'requests',
             'requests_ntlm',
             'pypac'
             
    ],
    
    dependency_links=[
     # "http://peak.telecommunity.com/snapshots/",
    ],
    
    extras_require={
    },
)
