# :one: DAHENG CAMERA on raspberry 4
## **What we need**
>### PyEnv instalation
> >  sudo apt update && sudo apt upgrade    
> >  sudo apt install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev    
> >  git clone https://github.com/yyuu/pyenv.git ~/.pyenv
> >  sudo nano ~/.bash_profile    
> > --- **Write this in bash.profile**    
> >  export PYENV_ROOT="$HOME/.pyenv"    
export PATH="$PYENV_ROOT/bin:$PATH"    
eval "$(pyenv init -)"    
> > --- **Reload .bash_profile.**    
> > source ~/.bash_profile    
>### Python instalation    
> > pyenv install 3.7.0    
> > --- **Set python3.7 to global** 
> > pyenv global 3.7.0      
> > :white_check_mark: The maximum version of Python is 3.7, because starting from 3.8 the dll import won't work in this example.    
>### Installing the OpenCV, numpy and pillow    
> > sudo apt-get install build-essential cmake pkg-config    
> > sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev    
> > sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev    
> > sudo apt-get install libxvidcore-dev libx264-dev    
> > sudo apt-get install libgtk2.0-dev libgtk-3-dev    
> > sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev    
> > sudo apt-get install libfontconfig1-dev libcairo2-dev    
> > sudo apt-get install libatlas-base-dev gfortran    
> > sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103    
> > sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5    
> > pip install opencv-contrib-python    
> > pip install numpy    
> > pip install pillow    
>### Installing the Daheng SDK for arm    
> >  [ Linux ARM SDK USB3+GigE v1.4.2206.9161](https://www.get-cameras.com/customerdownloads?submissionGuid=d07dff37-9898-4c4e-b892-5eec82915141) : download and extract zip files     
> >  cd _Your folder name_      
> >  cd _next folder_    
> >  cd api    
> >  sudo python setup.py build    
> >  sudo python setup.py install    
> >  
## **Using python scripts to start catch images from Daheng Camera**    

