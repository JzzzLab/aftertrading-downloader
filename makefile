RMDIR = rm -rfv
README = README.md
REFRESH = refresh.bat
SWITCH_TO_CSV = switch to csv.bat
SWITCH_TO_MASTER = switch to master.bat
msg = renew
INIT_MSG = First commit: root
CSV_MSG = First commit: branch 'csv'
MASTER_MSG = First commit: branch 'master'
REPO = git@github.com:JzzzLab/aftertrading-downloader.git

.SILENT: all
all:
	echo waiting for a command

.PHONY: init
init:
	git init
	
	git add $(README)
	git add $(REFRESH)
	git commit -m "$(INIT_MSG)"

	git checkout -b csv
	git add "$(SWITCH_TO_MASTER)"
	git commit -m "$(CSV_MSG)"

	git checkout master
	git add -A
	git commit -m "$(MASTER_MSG)"

	git remote add origin $(REPO)
	git push -u origin master
	git push -u origin csv

.PHONY: rmgitdir
rmgitdir:
	$(RMDIR) .git/

.PHONY: gitcp
gitcp:
	git add -A
	git commit -m "$(msg)"
	git push

.PHONY: gitpa
gitpa:
	git pull --all