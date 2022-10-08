# Face recognition project

## find resources

video

## using Google Colab

- hide an output of a cell, Ctrl M O

## jupyter

installed anaconda

then used [this](https://jupyter.org/install)

## using virtual environment

[creation](https://janakiev.com/blog/jupyter-virtual-envs/), might face an [issue](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows) with powershell

```shell
pip install --user virtualenv
# to have the same name of this dir.
python -m virtualenv .
# to avoid error that might appear when execute it on powershell
Set-ExecutionPolicy Unrestricted -Scope Process
.\scripts\activate

```

when jupter does not render the output of the cell, image or other stuff, [just reload](https://stackoverflow.com/questions/68736618/error-loading-preloads-could-not-find-renderer) it 😜

## Fix GPU problem

download CUDA Toolkit and cuDNN SDK, simply follow [this](https://stackoverflow.com/questions/41402409/tensorflow-doesnt-seem-to-see-my-gpu)

## To add app folder to github

[how to add a folder to hithub](https://stackoverflow.com/questions/12258399/how-do-i-create-a-folder-in-a-github-repository)
