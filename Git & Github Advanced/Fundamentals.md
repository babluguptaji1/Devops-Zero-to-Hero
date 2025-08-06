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
// username for 'https://github.com' : put user name
// password for  'https://https://<repository username>@github.com : put here personal acess token

git remote -v // // for testing GitHub is connected with git
git remote set-url origin https://<personal Acess token>@github.com/username/repository name here.git // for many time use , no need to next time even use user name and password or don't ask you terminal nest time username and password. 
clear//
git push origin master
// * [new branch] master -> master
// pushes Done by git on GitHub repository
##########################################


git pull origin master // github data to git that is called pull from master github


for github push :
vim from_local.txt
git add from_local.txt
git commit -m "added from local"
ls
git branch
git push origin master
// master -> master 
 
//Note : git pull is not use in another person repository because you should token of  his repository. 

git remote -v // test
git clone <repository url>
ssh-keygen // generating public/private ed2...9 key pair (for pair my repository to Another person repository)
//Enter file in which to save the key (/home/ubuntu/.ssh/id_ed25519): enter press then
/home/ubuntu/.ssh/id_ed25519 already exists.
Overwrite (y/n)? ^c (Ctrl + C)
cd .ssh
ls
authorized_key  id_ed25519 id_ed25519.pub know_hosts known_hosts.old

.ssh$ cat id_ed25519
-----Begin openssh private key-----
aghshhshh...70(case form)
jsjhshshjbshshshsh..70 (case form)
aghshhshh...70(case form)
jsjhshshjbshshshsh..70 (case form)
aghshhshhhshhshehhdhdhdhjddh
-----End openssh private Key-------

ssh$ ls
authorized_key  id_ed25519 id_ed25519.pub know_hosts known_hosts.old

ssh$ cat id_ed25519.pub
ssh-id25519 GSKGKGSKSKGKGDKGSKSKDGKDGKGKSGKS
A ubuntu@ip-172-31-34-159 // copy this code go github > profile> ssh and GPG KEYS >NEW SSH KEY:
TITLE: ANYNAME EX:BATCH-9-SERVER-KEY
KEY TYPE : ATHENTICATION
KEY : PASTE HERE YOUR COPY 🔑 KEY (EX: ssh-id25519 GSKGKGSKSKGKGDKGSKSKDGKDGKGKSGKS
A ubuntu@ip-172-31-34-159)
 >Add ssh key
>go terminal:
ls
mkdir github_repo
cd github_repo/
ls

go github> choose and copy any person repository url (ssh )
>go terminal:
git clone git@github.com:LondheShubham153/90DaysOfDevOps.git

yes

ls

cd 90DaysOfDevOps
ls
vim Readme.md
😊 you 💘 
git status
o/p > on branch master
git diff// for changing in document
git add Readme.md
git status 
git commit -m "added some changes"
git push origin master


# abhi hamne sikha ki kaise dusare ke repository ko clone kar sakte hai 

aayiye jante hai ki 
2:07:39

github  to github fork kiya jata hai clone karne ke liye

repository choose kar le  pahle

git clone origin master //for self

and that choose any file for modify
ex: Readme.md

vim readme.md
this is readme file
esc
:wq
 
git status
Readme.md (Red : Untracked file)

//that i am want to not push on github main branch so that i make another branch name any  that you want you. 
// why we make another branch because my Readme file is not professional way 
//my readme file is look like Rough or simple tipe

 git checkout -b networking
git add .

make a file .gitignore for not want to publish on github Repository, or  i don't want to push on github repository

vim .gitignore
.Ds_store

>exit
git commit -m "added networking solution"
git push origin networking //networking is a subbranch

//but you can push with this method.

// you can put token on .gitignore file

## What SHOULD be in version Control?
1.Unit Tests
2.Build Scripts
3.Source Code
4.Documentation
5.Database Schema
6.Configuration files
7.Deployment Script
8. Kubernetes manifests
9. Docker and compose files
10.Infrastructure as Code (IaC) Files
11.Dependency Lock Files: e.g, package-lock.json


## What should Not be in Version Control?
1.Logs
2.Secrets
3.Build Artifacts
4.Large Binary Files
5.IDE or OS-Specific Files
6.Temporary or Cache Files

//Use Git tags to mark versions so you can navigate back or forth as needed.

Remember: Version control isn't about tracking code--it's a Blueprint of Entire Application.

terminal:
man git // for all git command list

# Branching Strategy #1
master/main // default Branch
// production branch 
production = master
testing = staging branch
Development = Dev Branch
Features = Feat /for new member 
Features🔀 >Development✳️ >testing♻️ >production✅️

merge another branch for push Best Quality code 

master can create another branch for Error code/ notFix 

notFix can merge with master and staging. 
Dev merge by staging, 
staging merge by Feature branch





