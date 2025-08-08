**Start Here:**

```markdown
# GitHub Advanced
* Pull Requests = merge Request🔄
* Revert & Reset🔄
* Stashing
* Cherry-Picking
* Rebasing
* Branching Strategies used in Companies

## Theory start Here:
Launch instance:
in Aws Ec2:


''git is version control system
founder of linux is create git''
git merge dev

pull request ✅️
Revert & Reset // is just like undo commit or wrong commit 
git log --oneline // to see all commit
git revert <commit Id>
git commit -m "some changes on commit"
again give conflict massage change some in file
using vim <name of here file>

git revert --continue //fix conflict and run command line

git revert --skip // to skip this patch⚠️
git revert --abort // to cancel the revert operation⚠️


git reset

git restore --staged

git stash & pupping 

git Stashing list

git stash pop 0

git cherry-Pick <commit id>

git rebase dev







## Git & Github CheatSheet

### Repository management


|    Command    | Description   |
| ------------- | ------------- |
| Git init      | Intialize a new repository  |
| git clone <repo  | clone an existing repository  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
git remote -v   // View remote repository
git remote add origin <url> // Link local repo to remote
Adding and community:
git add <file> //stage changes for commit
git add . // stage all changes
git commit -m "message" //commit changes with a message
git commit --amend // edit the last commit

Branching and Merging:
 git branch //List Branches
 git branch <branch> // create a new branch
 git checkout -b <branch> // create and switch to a new branch
 git merge <branch> // Merge a branch into current branch
 git branch -d <branch> Delete a branch
 git Checkout <branch> // Switch to a branch

 Log and History:

 git log   //view commit history
 git log --oneline // view commit history in one line
 git diff  // view unstaged changes
 git diff HEAD //compare working directory to HEAD

Undo changes:

git reset <file> unstages a file Changes remain in the working directory
git restore <file> //Restores a file to its last committed state
git reset --hard <commit> //Resets the current branch to the specified commit and discords all local changes.
git revert <commit> Create a new commit that undoes a previous commit


Pushing and pulling :

git push origin <branch> // Push changes to the remote repository
git pull origin <branch> // Pull changes from the remote repository


Log Git Config command :

git config --global user.name "<name>" //Sets the global username for git commits.
git config --global user.email "<email>" //Sets the global email for git commits.
git config --list // Display the current Git configuration (User details, editor, etc)

Git Status command:

git status // Shows the current status of the working directory and stagging area, indicates tracked, modified , untracked , or staged files

Git Fetch Command:

git fetch // downloads commits files and references from a remote repository without merging them into the local branch.


# Advanced Commands

Stashing Command: 

git stash // Save changes to a Stash
git stash list //List all stashes
git stash apply //Apply the lost stash
git stash drop //Delete the last stash

Rebase and Cherry-Pick:

git rebase <branch_name> //Reapplies commits on top of another base branch. It rewrite history. so avoid using it on shared branches.

git rebase -i <commit_hash> //Allows you to rebase interactively from a specific commit.

git rebase --abort // Aborts the rebase process and returns to the state before starting the rebase

git rebase --continue //continues the rebase after resolving conflicts

git rebase --skip // Skips the current commit during rebase.

git cherry-pick <commit_hash> Applies a specific commit from another branch to the current branch.

Tagging: 
git tag <tag> // Create a lightweight tag

git tag -a <tag> -m "msg"  //Create an annotated tag

git push origin --tags  // Push tags to remote


Git Bisect Command (Debugging to find Bad commits):

git bisect start // Begins the binary search to find the  commit that introduced a bug.

git bisect good <commit> //marks a known good commit (does not contain the bug) to start the bisecting process

git bisect reset //Ends the bisect process and resets the repository to the original state.

collaboration commands: 
git blame <file> //Shows who modified each line of the file.
git shortlog // summarizes contributions by author
git log --graph //visualize branch history
git show <commit> // Displays details of a specific commit
git diff --staged // Show differnce between staged changes and the last commit

# GitHub push Methods:
1. SSH Method:
--1.Generate on SSH key:
   using: `ssh-keygen`

--2.Copy the SSH key:
   using: `cat ~/.ssh/<key_name>.pub`

--3.Navigate to Github > Settings > SSH and GPG keys> New SSH key.

--4.Paste the key and save.

--5.Verify the SSH connection:
   using: `ssh-T git@github.com`

--6.Now clone the repo using ssh and do whatever you want  and add & commit the changes

--7.Push code:
   using:`git push origin main`

# 2.HTTPS Method
--1.Firstly Generate a Personal Access Token
--2.Use HTTPS URL for your repository:
   `git remote set-url origin https://<Your_PAT>@github.com/<username>/<repository_name>.git`
--3.Add and commit the changes
--4.Push code:
   `git push origin main/master`

   # Helpful Github Tips:
   
   ## Create Pull Request:
   1.Push <Your_branch> branch to github.
   2.Open the repository on Github.
   3.Go to the "Pull Requests" tab and click "New Pull Request"
   4.Select branches and create PR.

   GitHub Fork and Sync Workflow :

   1. Fork a Repository:
   a. Go to the repository on github and click on Fork.

   2. Clone the Fork:
    a.`git clone https://github.com/your-username/repo-name.git`
   3. Sync changes from Upstream:
    a.git remote add upstream https://github.com/original-owner/repo-name.git
    b.git fetch upstream
    c.git merge upstream/main

# Git Aliases :
Speed up your workflow by aliases:
1. git config --global alias.co checkout
2. git config --global alias.br branch
3. git config --global alias.ci commit

# GitHub Actions:
.Significance: Automates workflows like testing, building and deploying code.
.Example:
```yml Start here:
name: CI/CD Pipeline   #Name of the workflow
on:
 push:     #Triger workflow on push to main branch.
  branches:
   - main
 pull_request:
  branches:
   - main
jobs:
  build:       #Define a job name 'build'
   runs-on: ubuntu-latest   # Use the latest Ubuntu environment
steps:
 - name: Checkout Code
   uses: actions/checkout@v2
 - name: Install Dependencies
   run: npm install
   - name: Run Tests
   run: npm test

```Markdown

#  References:
 - Git Documentation
 - GitHub Docs




   
   
   
   









