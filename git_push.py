# git@github.com:nnuraip/Osnova.git
from os import system
system('clear')
ssh_url =  "git@github.com:nnuraip/Osnova.git"
branch = "master"
commit_message = "U"
try:
    system('git init')
    system('git add . ')
    system(f'git commit -m {commit_message} ')
    system(f'git remote add origin {ssh_url} ')
    system(f'git push -u origin {branch}')
except:
    print("somethig went wrong")
else:
    print("process was over succesfully")

