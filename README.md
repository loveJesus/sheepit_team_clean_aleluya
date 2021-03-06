####  For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# Sheepit Team Cleaner Aleluya

[SheepIt](https://sheepit-renderfarm.com) is a free distributed renderfarm for Blender. 
[Blender](https://blender.org) is the free and open source 3D creation suite. 

Sheepit allows the creation of teams, that are limited to 200 members. 
This program helps team administrators find team members that have not rendered anything in over 31 days
and will remove them from the team.

## Install and Run
```shell
pip install sheepit_team_clean_aleluya

# Assuming your python pip path is in $PATH 
sheepit_team_clean_aleluya -u <login username> -p <login password> -t <team id>
```

### Help
```text
usage: sheepit_team_clean_aleluya [-h] --team_id TEAM_ID_ALELUYA --username USERNAME_ALELUYA --password PASSWORD_ALELUYA [--dry_run] [--max_score MAX_SCORE_ALELUYA] [--min_score MIN_SCORE_ALELUYA]
                                  [--exclude_member EXCLUDED_MEMBERS_ALELUYA]

Log in to sheepit and remove members from a team that have not rendered in over 31 days, that are within a specified point range.

options:
  -h, --help            show this help message and exit
  --team_id TEAM_ID_ALELUYA, -t TEAM_ID_ALELUYA
                        The id of the team to clean
  --username USERNAME_ALELUYA, -u USERNAME_ALELUYA
                        Login username of team admin
  --password PASSWORD_ALELUYA, -p PASSWORD_ALELUYA
                        Login password of team admin
  --dry_run, -d         Dry run
  --max_score MAX_SCORE_ALELUYA, -M MAX_SCORE_ALELUYA
                        Max score of user that will still be removed
  --min_score MIN_SCORE_ALELUYA, -m MIN_SCORE_ALELUYA
                        Minimum score of user that will still be removed
  --exclude_member EXCLUDED_MEMBERS_ALELUYA, -X EXCLUDED_MEMBERS_ALELUYA
                        Members to exclude from being removed, can be placed several times
  --version, -v         show program's version number and exit

in Jesus Christ's name
```

### Notes:
Thank You Jesus for https://dzone.com/articles/executable-package-pip-install
```
pip install --upgrade pip setuptools wheel tqdm twine

python setup.py bdist_wheel

python -m pip install dist/sheepit_team_clean_aleluya-0.1.4-py3-none-any.whl

python -m twine upload dist/*
```
