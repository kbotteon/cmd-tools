# Notes

## Git

### Fixing line endings on a per-repo basis
Reverts line endings to those as they are stored in the repository.

```
git config core.autocrlf false
git rm --cached -r .
git reset --hard
```

### Searching across repos

To find all issues I opened that are still open:
```
is:open is:issue archived:false user:botteon
```

Substitute `user` for an Organization name to search that instead.

To find all open issues assigned to me:
```
is:open is:issue archived:false assignee:botteon
```

### Dealing with Submodules

To get Git to include submodule status by default:
```
git config --global status.submoduleSummary true
```

After switching to a new branch in the super-repo that contains new submodules:
```
git submodule update --init --recursive
```

## Adding files

Recursively by extension:
```
find . -name '*.pdf' -print0 | xargs -0 git add
```

## Linux

To check disk usage:
```
du -hc --max-depth=1 .
```

To check RAM usage for a user:
```
ps -U botteon --no-headers -o rss | awk '{sum+=$1} END {print int(sum/1024) "MiB"}'
```
