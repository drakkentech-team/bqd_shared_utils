# BQD SHARED UTILS
This is a sub-module for Bluerock Quality Database!
These will be modules and functions in common across larger modules.

### Setup ###
When cloning a parent module with this one inside of it,
make sure to run the following command from the parent directory:

```git submodule update --init --recursive```

Troubleshooting:
    - Make sure you have access writes on Github.
    - Should this fail to work and you get git fingerprint issues, you need to register yourr ssh key.
        1. Generate an ssh key on your system if it doesn't exist.
        2. Add your public ssh key to your Github account that has access to the submodule.

### Update ###
To get updates for this submodule, run the following command
from the parent directory:

```git submodule update --remote```

### Commiting ###
To commit changes to this as a submodule, you do your basic git commits
once you have navigate to this submodule's root directory.
