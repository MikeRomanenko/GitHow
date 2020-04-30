print("""
.gitingnore (to ingnore some files form being GITing)
git help config

**** set up GIT params ****
git config --global user.name "Your Name"
git config --global user.email "Youremail"
git config --list

**** Init the WORKING FOLDER ****

git init

***** Create a brach for the feature **** or work on master

git branch calc-devide
git checkout calc-devide

**** CLONE REPO ****
git clone <url> <where to clone>
or
git clone ../remote_repo.git .
or
git clone https://github.com/MikeTesting/ .

git remote -v
git branch -a

**** WORKING COMMANDS ****
git diff
git status
git add -A
git commint -m "Updating the build number"
got log

*** PUSHING CHANGES ***
git pull origin(our repo) master(branch to push to)
git push origin(our repo) master(branch to push to)

*** Push branch to Remote *** - after commit

git push -u origin calc-divide
-u  -means that it will save this branch as the default option to work with
git branch -a

*** MERGE BRANCH WITH MASTER ***

git checkout master
git pull origin master
git branch --merged
get merge calc-divide
git push origin master

*** DELETE the branch e.g. ***

git branch -d divide
git push origin --delete divide  - for REMOTE
""")
