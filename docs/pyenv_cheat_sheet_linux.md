# pyenv-virtualenv cheat sheet

## instructions to nuke your previous anaconda installation

Lora Johns wrote the [Mac version](https://github.com/lorarjohns/awesomeVenvs). This is a close copy translated for Linux (specifically, my Mint 19.2 system).

1. Install and run the Anaconda uninstaller

```sh
conda install anaconda-clean && anaconda-clean --yes
```

2. Find leftover directories and remove them (with rm -rf, or more conservatively)

```sh
grep -iR "Anaconda3" ~
```

3. Check your .bashrc, .bash_profile, or equivalent login profile and delete the conda init lines added by "Anaconda.3 xxxx.xx installer" and anything anaconda-related in your path.

4. Restart your shell.

```sh
source ~/.bashrc
```

## install pyenv and pyenv-virtualenv (Linux instructions)

1. Install pyenv and pyenv-virtualenv from source. 

You can clone the GitHub repos (instructions in their READMEs), but running pyenv-installer may be more convenient.

```sh
curl https://pyenv.run | bash
```

2. configure pyenv and pyenv-virtualenv

```sh
echo 'export PYENV_ROOT= "$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH=$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

3. install python versions with pyenv

- get a list of options: `pyenv install --list`
- remove a version: `pyenv uninstall`
- install a version: `pyenv install`

4. set your global and local pythons

- set your global python: `pyenv global 3.x.x`
- set your local (project) python--**important** for venv switching! `pyenv local 3.x.x`
- set a version for the current shell: `pyenv shell 3.x.x`
- use a one-off python module or command: `pyenv exec python [-m, -c]`

5. create and activate virtual environments

- set local python: `pyenv local 3.x.x` or `pyenv local anaconda xxxx.xx`
- make a venv: `pyenv virtualenv 3.x.x name-of-your-new-venv`
- set and activate: `pyenv local name-of-your-new-venv && pyenv activate name-of-your-new-venv`
- if you used conda: `conda activate your-new-conda-env`

## Optional helpful pyenv management

- To prevent old Python 2 habits creeping in by mistake, alias virtualenv to pyenv virtualenv

```sh
echo 'alias virtualenv="pyenv virtualenv"' >> ~/.bashrc
```

- Delete virtual envs created with pyenv: `pyenv uninstall venv-name` or `rm -rf venv-directory`

## Set up Visual Studio Code for Python and Jupyter

1. [Get VSCode](https://code.visualstudio.com/docs/setup/linux). I used snap: `sudo snap install --classic code`, but it's probably easier to download and run [the deb package](https://go.microsoft.com/fwlink/?LinkID=760868) or the equivalent for other distributions.
2. Install and enable the [Python extension](https://github.com/Microsoft/vscode-python)
3. In VSCode, open the command palette (command+shift+P) and configure the Terminal options to integrate with the system terminal (e.g., zsh and iTerm2)

- vscode will now inherit your venvs and automatically switch them with pyenv virtualenv

4. In VSCode, open the command palette (command+shift+P) and choose `Shell command: Install 'code' command in path`

- now you can open files and directories from the command line with `code .`, `code file.py`, `code. /path/to/stuff/`, etc.

5. launch a project directory with anaconda or jupyter enabled with `code /path/to/project`.
6. command+shift+P `Python: Create New Blank Jupyter Notebook` (or open an existing one, if you like)
7. convert notebooks to .py scripts with one click

## More VSCode fun

- use github integration (pull, diff, merge, push) directly from the editor
- install themes with syntax highlighting, code linters, testing, and more tools
- polyglot code support!