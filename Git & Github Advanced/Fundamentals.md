# Fundamentals
```git 
git --version //for checking version
Example: git version 2.43.0

cd scripts  //for changing directory
 ls // view directories and files
 rm <file name> // for remove file
 git init // file or directory ---> to ---> version control system (git)
git status // check file condition : untracked or tracked or commited
git add ./<file Name Here> // for stagged (green)
git rm --cached <file neme here> // for unstage ( green --> red)
git commit -m "Addec Readme.md" // for save your file in directory
git restore readme.md // for backup deleted file in your repository, but without git init directory is not work command line but you can restore from recyclebin
git restore --staged readme.md // for unstage
git config --global user.name "technical Asthavi" // add user name of your repository
git config --global user.email "technicalasthavi@gmail.com" // add user email of your repository
clear // clear windows terminal commands
history // terninal give you all command list that you have uses in terminal
 Note : if You have not available file for commit,Your Terminal says to you: " Your working tree is clean"
cd .. // for child directory to parrent directory
Note : if you have not uses git init command in directory , Terminal says : fatal: not a git repository (or any of the parent directories): .git
git branch // to see branches and * (star) is indicate you You are working here.
git checkout -b Dev // for Switched to a new branch "Dev" name
-----when you put command under Dev (Branch) : git status // Terminal say : On Branch Dev nothing to commit, working tree clean. and (-b ) use for new branch create.
-----ls // your all dir/file see in subdirectory (Dev) or  main files or dir copy to Dev branch
-----vim from_Dev.txt --> This is a file in the Dev Branch -->esc --> :wq --> Back to Terminal
-----git status // On Branch dev    from_Dev.txt  --> untracked
------git add from_Dev.txt //stages --> git commit -m "added Dev file" -->
      Next : --> git branch // to see branch
     ex: *Dev
          master
git checkout master// to move main branch // branch is a seperate line of branches
Note : sub branch is not copy your dir or file when you want to move parrent branch(master)

git log --oneline // to see comment list with id and massages
and (HEAD -> master) is notify to you : you have recently added this commit


git checkout dev // to switched dev branch
or
git switch Dev // to switched dev branch

git checkout -b staging // for create new branch (name = staging) and moved to new branch Staging

for mergging branch :

git merge dev // dev branch copy folder -- to -- master branch // that means main branch update by Dev Branch for commitable file // sure ! before this changes you must to switched master branch then try it.

Access
1. Personal Access Token
2. SSH

git remote -v // to varify your git repository is connected to GitHub // if yes : see in Terminal // if no: terminal give no any information. that means black .

git remote add origin <repository url> // for stablish connection with git Terminal to Github Repository

again

git remote -v // for see connection :
 output : origin <repository url (show here in https method  formate)> (fetch)   
 output : output : origin <repository url (show here in https method  formate)> (push)

git status
// on branch master
// nothing  to  commit, working tree clean

git push origin master
// userrname for 'https://github.com' :
// password for  'https://https://<repository username>@github.com :


