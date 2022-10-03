# DAHENG CAMERA on raspberry 4
## :white_check_mark: **What we need?**
>### :one: PyEnv instalation
> >  :black_small_square: sudo apt update && sudo apt upgrade    
> >  :black_small_square: sudo apt install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev    
> >  :black_small_square: git clone https://github.com/yyuu/pyenv.git ~/.pyenv
> >  :black_small_square: sudo nano ~/.bash_profile    
> > --- **Write this in bash.profile**    
> >  export PYENV_ROOT="$HOME/.pyenv"    
export PATH="$PYENV_ROOT/bin:$PATH"    
eval "$(pyenv init -)"    
> > --- **Reload .bash_profile.**    
> > :black_small_square: source ~/.bash_profile    
>### :two: Python instalation    
> > :black_small_square: pyenv install 3.7.0    
> > --- **Set python3.7 to global**   
> > :black_small_square: pyenv global 3.7.0      
> > :warning: The maximum version of Python is 3.7, because starting from 3.8 the dll import won't work in this example. :warning:    
>### 3️⃣:Installing the OpenCV, numpy and pillow    
> > :black_small_square: sudo apt-get install build-essential cmake pkg-config    
> > :black_small_square: sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev    
> > :black_small_square: sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev    
> > :black_small_square:  sudo apt-get install libxvidcore-dev libx264-dev    
> > :black_small_square: sudo apt-get install libgtk2.0-dev libgtk-3-dev    
> > :black_small_square: sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev    
> > :black_small_square: sudo apt-get install libfontconfig1-dev libcairo2-dev    
> > :black_small_square: sudo apt-get install libatlas-base-dev gfortran    
> > :black_small_square: sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103    
> > :black_small_square: sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5    
> > :black_small_square: pip install opencv-contrib-python    
> > :black_small_square: pip install numpy    
> > :black_small_square: pip install pillow    
>### 4️⃣:Installing the Daheng SDK for arm    
> > :black_small_square: [ Linux ARM SDK USB3+GigE v1.4.2206.9161](https://www.get-cameras.com/customerdownloads?submissionGuid=d07dff37-9898-4c4e-b892-5eec82915141) : download and extract zip files     
> >  :black_small_square: cd _Your folder name_      
> >  :black_small_square: cd _next folder_    
> >  :black_small_square:  cd api    
> >  :black_small_square: sudo python setup.py build    
> >  :black_small_square: sudo python setup.py install    
> >  
## :white_check_mark: **Using python scripts to start catch images from Daheng Camera**    

