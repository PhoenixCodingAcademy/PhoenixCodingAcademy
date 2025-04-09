<!--
DESCRIPTION: Here is a list of Git commands that you can run from any terminal or console.
-->
[TOC]

Here is a list of Git commands that you can run from any terminal or console.


# Initialization

There are two ways to create a Git folder on your local machine:
1. **Create New Repository**: Create a new empty repository in the current folder:
   ```bash
   git init
   ```

2. **Clone Existing Repository**: Copy an existing repository from somewhere else:
   ```bash
   git clone <repository url>
   ```
   For example:
   ```bash
   git clone https://github.com/username/repository.git
   ```

# Notes

```
Git

github accounts
* rshphx


DOWNLOAD
http://download.tortoisegit.org/tgit/

SCHEMA
https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object
https://stackoverflow.com/questions/10986615/what-is-the-format-of-a-git-tag-object-and-how-to-calculate-its-sha
https://stackoverflow.com/questions/22968856/what-is-the-file-format-of-a-git-commit-object/37438460#37438460
https://stackoverflow.com/questions/7225313/how-does-git-compute-file-hashes/7225329


mkdir git
cd git
git init
git checkout HIC
git remote set-url origin //HP7/git
git remote add origin //HP7/git

git pull origin HIC
git push origin HIC



# CONFIG
git config --global user.name "robertscotthoward"
git config --global user.email "rob@willo.org"
git config --global core.editor "textpad"
git config --global color.ui true
git config --list
git config --global core.autocrlf false
  --> Sometimes after restoring a file, the status still shows modified. This can correct that.

PROBLEM: The file will have its original line endings in your working directory.
SOLUTION: git config core.autocrlf true

# Get the URL that cloned this directory.
git config --get remote.origin.url

#BASH
TO FIX:
  WARNING: terminal is not fully functional
  $ export TERM=msys

# SET PROMPT
.bash_profile
__git_ps1

# HELP
git help

# INIT
Change to your folder and...
git init
  -> Creates a .git folder in it.

# INIT BARE
git init --bare
  -> Creates a .git folder in it.
SEE: http://www.saintsjd.com/2011/01/what-is-a-bare-git-repository/

git clone --bare REPO

# Set the default branch in a bare repo:
git symbolic-ref HEAD refs/heads/MYBRANCH


# STATUS
Tell us the difference between our working, staging, and repository:
git status

For all branches:
git branch -avvv


Show all local branches sorted by descending date.
git for-each-ref --sort=-committerdate refs/heads/

LOCAL
git for-each-ref --sort=-committerdate refs/heads/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'

REMOTE
git for-each-ref --sort=-committerdate refs/remotes/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - [%(authorname)] (%(color:green)%(committerdate:relative)%(color:reset))'


STATISTICS

git shortlog -s -n -e

git log --encoding=utf-8 --full-history --reverse "--format=format:%at;%an;%ae" | git-authors

git log -1 --pretty="format:%ci" ./projects/web/templates/_template.html
git log -1 --date=short --pretty="format:%ad (%h) %an: %s" ./projects/web/templates/_template.html
find . -type f | grep -v .git | head | xargs -I {} git log -1 --date=short --pretty="format:%ad (%h) %an: %s" {}




# DIFF
git diff
git diff --staged
git diff --cached


#DELETE/REMOVE A FILE
git rm FILE.TXT

# REMOVE A FOLDER
git rm -r FOLDER

#RENAME / MOVE A FILE
git mv FILE.TXT NEWFILE.TXT

#RESTORE THE FOLDER TO A REPOSITORY
git checkout -- FILE.TXT
-- means to stay on the current branch; do not interpret FILE.TXT as the name of a branch.

#RESET LOCAL BRANCH TO MATCH REMOTE
git fetch origin
git reset --hard origin/master

#UNDO MODIFIED FILES
git reset --hard

#UNSTAGE (UNDO) A FILE
git reset HEAD FILE.TXT

#UNSTAGE (UNDO) ALL
#Suppose you just executed "git add ." and you want to undo it:
git reset

#UNDO A STAGING
git checkout -- FILE.TXT

# CHECKOUT MOST RECENT
git checkout -

# UNDO MERGE NOT PUSHED
git reset --hard HEAD~1

#RESET ENTIRE FOLDER
git reset --hard HEAD
git clean -f
git checkout .


# Go back to a previous COMMIT and continue from there.
git checkout COMMITSHA1
Only the first few bytes of COMMITSHA1 are needed.

# Revert: do commit automatically
git revert COMMITSHA1

# Revert: do NOT commit automatically
git revert COMMITSHA1 -n

# GET A FILE FOR A SPECIFIC COMMIT
git checkout 818789ef /c/HomeSmart/RealSmartApplications/Broker/Broker.csproj


# WARNING: Reset. Sets HEAD to a specific commit
git reset --soft COMMITSHA1  # does not change stage and work
git reset --mixed COMMITSHA1  # default: does change stage but not  work
git reset --hard COMMITSHA1  # default: changes stage and work

# REMOVE UNTRACKED FILES
git clean -n # Test run
git clean -f # Do it

# TRACK TO FOLDER
git branch --set-upstream-to=origin/master feature/RA-1709


# IGNORE
.gitignore
https://github.com/github/gitignore

To be global to all repositories:
git config --global core.excludesfile ~/.gitignore_global

Tell git to stop tracking a file:
git rm --cached build.txt

To track a folder, it must have a file in it.
Tell git to track a folder:
Just put a .gitkeep (or any file) in that folder
touch FOLDER/.gitkeep


#APPEND THE MOST RECENT COMMIT
git commit --amend -m "Bad message"
git commit --amend -m "Updated message"


# ONEDRIVE REMOTE EX POST FACTO
You have a local project.
You "git init" it and track changes there.
Now you want it in a remote repos
Create "D:\Users\Rob\OneDrive\Projects\repos\ng5\spec"
git init --bare

In local project folder:
git remote add origin /c/Users/rob/OneDrive/Projects/repos/ng5/spec
git remote add origin/master

# Show all the remote branches
git ls-remote

# Show remote URL where the folder was cloned from:
git remore show origin
git config --get remote.origin.url

git remote add origin ~/Dropbox/repos/node/phxlib
git add .
git commit -m "Init"
git push -u origin master

THEN: git fetch/pull/fetch from then on...

ERROR: error: src refspec master does not match any.
CAUSE: You probably forgot to add . and commit the first time.

git push -u origin master
  Same as:
    git push --set-upstream origin master

git branch --set-upstream-to=origin/master

# AUTHENTICATION

git remote set-url origin git@github.com:robertscotthoward/mapa.git


# SUBMODULES

In your git repo project:

git submodule add ~/Dropbox/repos/tools

git pull --recurse-submodules



# FORK
Alice has a repo. You like it. You want to use it.
You (Bob) can clone it to your workspace (which defines origin to Alice), but you cannot push back to it because Alice owns it.
Better, you fork it as Bob (which defines origin to Alice). Then you clone from Bob to your workspace (which defines origin to Bob).
You will then want to set its upstream pointer to Alice
  git remote add upstream git://github.com/Alice/repo.git
Now you can push back to your fork, but create a pull request for Alice.

SEE: http://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-in-github/9257901#9257901
SEE: //stackoverflow.com/questions/2739376/definition-of-downstream-and-upstream/2749166#2749166

# Create an upstream branch
git remote add upstream \\HP7\git

# CLONE
# Make a new repository from cloning a remote server so you can push changes back to it.
git clone \\HP7\git
git clone \\HP7\git
git branch -a
git checkout HIC

remote HEAD refers to nonexistent ref, unable to checkout.

# WORKFLOW
Make a change to the folder
Put them in the staging area:
  git add .
Commit to repository:
  git commit -m "My first commit"




# LOG
git log --graph
git log --graph --pretty=oneline --abbrev-commit
git log --graph --pretty=format:"%h%x09%an%x09%ad%x09%s" --abbrev-commit
git log origin/master..
git reflog
git reflog --date=iso


git log --oneline --graph --decorate --left-right --boundary --date-order remotes/master..remotes/Span

# LOG TREE
git log --graph --simplify-by-decoration --pretty=format:'%d' --all
git log --graph --oneline --decorate --all

Show recent changes
git log --pretty=format:"%h%x09%an%x09%ai%x09%s"
  See https://git-scm.com/docs/pretty-formats
git log -n 5
git log --since=2012-12-31
git log --until=2012-12-31
git log --author="Rob"
git log --grep="Bug"
git log --oneline py/makefiles.py
git log --oneline --graph --all --decorate
  --since="2014-03-31"
  --until=3.days
  --until=2.weeks
  --author="Rob"
  --grep="bug"
  --stat
  --summary
  --format=oneline
  --format=short
  --format=medium
  --format=full
  --format=fuller
  --format=email
  --format=raw
  --format=graph
  --all
  --decorate

Show
for branch in `git branch -r | grep -v HEAD`;do echo -e `git show --format="%ci %cr" $branch | head -n 1` \\t$branch; done | sort -r


List all repositories
curl -s https://api.github.com/users/robertscotthoward/repos?per_page=1000 |grep git_url |awk '{print $2}'| sed 's/"\(.*\)",/\1/'
curl -s https://api.github.com/users/DigitalGarage1/repos?per_page=1000 |grep git_url |awk '{print $2}'| sed 's/"\(.*\)",/\1/'


#SHOW
git show HEAD
git show f5a59b5e


#CHERRY PICK
git cherry-pick f5a59b5e


#DIFF - Compare Two Branches
git diff f8af37e
git diff f8af37e..f8af37e^^
  -b ignore space changes
  -w ignore all space changes
  --color-words

git diff f8af37e..f8af37e
  That will produce the diff between the tips of the two branches. If you'd prefer to find the diff from their common ancestor to test, you can use three dots instead of two:
git diff f8af37e...f8af37e



#HISTORY
gitk /c/HomeSmart/RealSmartApplications/RealSmartApplications.sln
git log -p -- /c/HomeSmart/RealSmartApplications/RealSmartApplications.sln

#BRANCHING
List:
git branch

# Branch tracking?
git branch -vv

Make new:
git branch NEWBRANCHNAME

Show all branches that are in this branch:
git branch --merged
git branch --merged BRANCHNAME

Move/Rename a branch
git branch -m (or --move) OLDNAME NEWNAME

Switch:
git checkout BRANCHNAME

Make a switch in one step:
git checkout -b NEWBRANCHNAME

Delete a branch
git branch -D BRANCHNAME

Abandon all changes in branch
git checkout master
git reset --hard HEAD
git reset --hard origin/master

git reset --hard master


Example:
git checkout master
git reset --hard origin/master


# STASH (Like TFS shelve)
git stash                            # Saves the current state under a generated name
git stash save "My shelf name"       # Saves the current state under a given name
git stash list
git stash show stash@{0}
git stash show -p stash@{0}
git stash pop   # Leaves the copy in stash. Pulls the first one
git stash pop stash@{1} # Pulls the second one
git stash drop stash@{1}
git stash clear


# MERGING

git mergetool tool=""

# Merge mybranch into master:
git checkout master
git merge mybranch

# Merge in remote branch
git fetch origin main:main
git fetch <remote> <sourceBranch>:<destinationBranch>


# CONFLICTS
Abort the merge:
git merge --abort

Else edit the file in conflicts,
manually remove the merge tags,
git add the file, and commit.


# REBASE
git rebase --abort
git pull --rebase

git pull --rebase
  A shorthand for git fetch and then a plain git rebase, so the only difference is that applying only the latter would not fetch any new commits from your remote prior to rebasing your code on top of, as it would only take into account what's your repository already aware of.

# REMOTE: List remote servers
git remote -v

git fetch \\HP7\git

All git fetch does is update your local copy of a remote branch. This local copy doesn't have anything to do with any of your branches, and it doesn't have anything to do with uncommitted local changes. I have heard of people who run git fetch in a cron job because it's so safe.

# Create a short name
git remote add pb git://github.com/paulboone/ticgit.git
git remote add hp7 \\HP7\git



Start git service.
git daemon --export-all

Connect from remote machine:

git ls-remote git://hp7/py
git clone git://hp7


# TREE-ISH
A treeish is a reference to a commit; e.g.
a 40-character SHA1
or any short prefix of it (e.g. 4 to 10 characters)
or a HEAD pointer
or a branch reference
or a tag reference
or ancestor; eg. -HEAD^ means the parent of HEAD; or -HEAD~1
or the grandparent -HEAD^^ or -HEAD~2

git ls-tree HEAD
git ls-tree HEAD py/tools/



GITHUB

KEYPAIR SSL
ssh-keygen -t rsa -b 4096 -C "rob@willo.org"
--or--
keygen -t rsa -b 4096 -C "rob@willo.org"
ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub

C:\Users\rhoward\.ssh

git push prompting for username and password?
  git remote set-url origin git@github.com:PhoenixCodingAcademy/PhoenixCodingAcademy.git


REVOCATION
The revocation function was unable to check revocation for the certificate
https://stackoverflow.com/questions/45556189/git-the-revocation-function-was-unable-to-check-revocation-for-the-certificate
git config --global http.sslBackend openssl
git config --global http.sslVerify true


CERTIFICATE

PROBLEM: SSL certificate problem: unable to get local issuer certificate
SOLUTION: git config --global http.sslVerify false



================================================================================
These commands will set up the git defaults:

git config --global alias.l   "log --pretty=format:'%h %Cgreen%ad%Creset %an %Cgreen%s%Creset' --date=format:'%a %Y-%m-%d %I:%M %p'"
git config --global alias.lr  "log --pretty=format:'%h %Cgreen%ad%Creset %an %Cgreen%s%Creset' --date=format:'%a %Y-%m-%d %I:%M %p' origin/master"
git config --global alias.ll  "log --graph --oneline --decorate --branches --tags"
git config --global alias.lll "log --graph --oneline --decorate --all"

# List all branches sorted by last commit.
git for-each-ref --sort=-committerdate refs/remotes/ --format='%(committerdate:iso8601) %(refname:short) %(authorname)'
git config --global alias.bl  "for-each-ref --sort=-committerdate refs/heads/"
git config --global alias.thishist "for-each-ref --sort=-committerdate refs/heads/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'"

git config --global alias.thathist "for-each-ref --sort=-committerdate refs/remotes/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - [%(authorname)] (%(color:green)%(committerdate:relative)%(color:reset))'"

git config --global alias.unstage "'reset HEAD --'"


================================================================================
List settings:

git config --list --show-origin

================================================================================
.gitconfig

[user]
	name = Robert Howard
	email = RHoward@petsmart.com

[alias]
# https://git-scm.com/docs/pretty-formats
# https://stackoverflow.com/questions/7853332/how-to-change-git-log-date-formats
    l   = log --pretty=format:'%h %Cgreen%ad%Creset %an %Cgreen%s%Creset' --date=format:'%a %Y-%m-%d %I:%M %p'
    lr  = log --pretty=format:'%h %Cgreen%ad%Creset %an %Cgreen%s%Creset' --date=format:'%a %Y-%m-%d %I:%M %p' origin/master
    ll  = log --graph --oneline --decorate --branches --tags
    lll = log --graph --oneline --decorate --all

    thishist = for-each-ref --sort=-committerdate refs/heads/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'

    thathist = for-each-ref --sort=-committerdate refs/remotes/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - [%(authorname)] (%(color:green)%(committerdate:relative)%(color:reset))'

[http]
	sslBackend = openssl
	sslVerify = false


AZURE DEV OPS
https://dev.azure.com/genmicro/mapa

git clone https://username:password@github.com/username/repository.git
git clone https://anything:PAT@dev.azure.com/genmicro/mapa/_git/mapa
```


