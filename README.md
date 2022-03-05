####  For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# Sheepit Team Cleaner Aleluya

[SheepIt](https://sheepit-renderfarm.com) is a free distributed renderfarm for Blender. 
[Blender](https://blender.org) is the free and open source 3D creation suite. 

Sheepit allows the creation of teams, that are limited to 200 members. 
This program helps team administrators find team members that have not rendered anything in over 31 days
and will remove them from the team.

## Install and Run
```
pip install sheepit_team_clean_aleluya

# Assuming your python pip path is in $PATH 
sheepit_team_clean_aleluya
```

### Notes:
Thank You Jesus for https://dzone.com/articles/executable-package-pip-install
```
pip install --upgrade pip setuptools wheel tqdm twine

python setup.py bdist_wheel

python -m pip install dist/sheepit_team_clean_aleluya.0.1.whl

python -m twine upload dist/*
```
