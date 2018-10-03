# cxxopts

cxxopts is a C++ comand line option parser used by the
[Platform](https://github.com/PaladinAI/ddat-platform).

# Syncing with the upstream master branch

First, make sure the `upstream` remote is configured:

    git remote -v

    # If the upstream remote doesn't exist, add it:
    git remote add upstream https://github.com/jarro2783/cxxopts.git

Then merge the upstream changes from the `master` branch:

    git fetch upstream
    git checkout develop
    git merge upstream/master

# Publishing to the Conan server

To update the package, update the version number in `conanfile.py` then run:

    conan create . paladin/develop
    conan upload cxxopts/2.1.1@paladin/develop -r paladin
