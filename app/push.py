from subprocess import call

call(['git','add','-A',':/'])
call(['git','commit','-a','-m','"updating"'])
call(['git','push'])
call(['git','push','heroku','master'])
