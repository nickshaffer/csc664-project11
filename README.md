# csc664-project11
Automated tuberculosis interpretation using CNNs

# Our teams information
| Student Name | Student Email  	| GitHub Username |
|    :---:     |     :---:      	|     :---:       |
| Kristopher Phillips      |kphillips1@mail.sfsu.edu	|   krispy1994    |
| Nicholas Shaffer      |nshaffer1@mail.sfsu.edu	|   nickshaffer   |

# Model
Faster R-CNN ResNet-50 FPN

# Installations
* pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
* pip install detecto

# Running program
* run cnn.py
* you will be prompted to enter 1, 2, or 3
    * 1 will train new weights and save them using a batch size of 4, epochs of 10, and a learning rate of 0.01
        * since there are no weights if you first run this program, you should pick 1 to train new weights
    * 2 will predict an image from a folder of your choice
        * folder 1 will be images from kaggle with TB
        * folder 2 will be images from kaggle without TB
        * folder 3 will be images from the internet
        * folder 4 will be your own images 
            * it will start empty
        * after an image is predicted, enter 2 to predict the next image or 3 to stop predicting
    * 3 will exit the program

# Predicting your own images
* drag image into "images - your own" folder
* when you run the program, select 2 to predict an image, then select 4 for the folder with your own images


# Credit
Assets taken from [alankbi/detecto](https://github.com/alankbi/detecto)

