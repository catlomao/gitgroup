![gitgroup](https://raw.githubusercontent.com/catlomao/gitgroup/refs/heads/main/gitgroup.png)
# gitgroup
A multiplex Git management tool (gitgroup)
## install using
```
sh -c "$(curl -sS https://raw.githubusercontent.com/catlomao/gitgroup/refs/heads/main/installer.sh)"
```
```
usage: gitgroup [-h] add rm ls init run

A multiplex Git management tool (gitgroup)

positional arguments:
  add         adds repo to group
  rm          removes a repo from group
  ls          list all repos in group
  init        initializes the current folder (.gitgroup.json)
  run         executes git commands for each repo EXAMPLE <gitgroup run <git command like status or
              push whatever> >

options:
  -h, --help  show this help message and exit
```
