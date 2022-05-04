# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:03:06 2022

@author: AJ
"""
from docopt import docopt

# In[145]:
usage ="""
    Lane Lines Detection pipeline
    How to use ::
    1-run main.py file via anaconda cmd
    2-use Jupyter to run Jupyter_notebook.ipynp and edit the input & output pathes as you like

    Usage:
        Vehicle_Detector.py [-o]
        Vehicle_Detector.py [-v] [-o]<INPUT_PATH> <OUTPUT_PATH>

    Options:

    -h --help                               show this screen
    -v                                 process video file instead of image
                
    Ex: for single image input
    >>python main.py C:/test.jpg D:/out.jpg

    Ex: for video input
    >>python main.py --video C:/test.mp4 D:/out.mp4                
    """
    
def main():
        args = docopt(usage)
        input = args['<INPUT_PATH>']
        output = args['<OUTPUT_PATH>']

        
        if args['-v']:
            print ('this is V args')
        if args['-o']:
             print('this is H arg')
             print(args)
        
        else:
            print('this is image args')
            print('Image is done..!!')


if __name__ == "__main__":
        main()
