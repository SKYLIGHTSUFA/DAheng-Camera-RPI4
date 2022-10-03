# DAHENG CAMERA on raspberry 4
## **What we need**
>### PyEnv instalation
> >  sudo apt update && sudo apt upgrade    
> >  sudo apt install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev    
> >  git clone https://github.com/yyuu/pyenv.git ~/.pyenv
> >  sudo nano ~/.bash_profile    
> > **Write this in bash.profile**    
> >  export PYENV_ROOT="$HOME/.pyenv"    
export PATH="$PYENV_ROOT/bin:$PATH"    
eval "$(pyenv init -)"*    
:white_check_mark: The maximum version of Python is 3.7, because starting from 3.8 the dll import won't work in this example.    
