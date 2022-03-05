# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='sheepit_team_clean_aleluya',  
     version='0.1',
     scripts=['sheepit_team_clean_aleluya'] ,
     author="Love Jesus",
     author_email="loveJesus@loveJesus.xyz",
     description="Hallelujah - Help Sheepit Renderfarm team administrators clean users that have not recently rendered.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/loveJesus/sheepit_team_clean_aleluya",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GPL3",
         "Operating System :: OS Independent",
     ],
 )
