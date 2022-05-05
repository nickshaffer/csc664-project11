# Automated tuberculosis interpretation using CNNs

## Project Description & Learning Goals
Tuberculosis (TB) is an infectious disease usually caused by Mycobacterium tuberculosis (MTB) bacteria. Most infections show no symptoms and it is also time consuming to manually interpret each image to decide whether the patient is affected or not. Therefore, automation in interpretation and detection of this disease is important. In this project, you will apply a deep learning technique (convolution neural networks) to detect and classify patterns in such images.


## Our teams information
| Student Name | Student Email  	| GitHub Username |
|    :---:     |     :---:      	|     :---:       |
| Kristopher Phillips      |kphillips1@mail.sfsu.edu	|   krispy1994    |
| Nicholas Shaffer      |nshaffer1@mail.sfsu.edu	|   nickshaffer   |

## Model
Faster R-CNN ResNet-50 FPN

## Installations
* pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
* pip install detecto

## Running program
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

## Predicting your own images
* drag image into "images - your own" folder
* when you run the program, select 2 to predict an image, then select 4 for the folder with your own images

### Credit
Assets taken from [alankbi/detecto](https://github.com/alankbi/detecto)

### Data
https://www.kaggle.com/saife245/tuberculosis-image-datasets

### References
1. K. P. Smith, A. D. Kang, and J. E. Kirby, Automated Interpretation of Blood Culture Gram Stains by Use of a Deep Convolutional Neural Network, Journal of Clinical Microbiology , 2018, 56 (3) e01521-17.
2. C. Szegedy, W. Liu, J. Yangqing, P. Sermanet, et al. Going deeper with convolutions. The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 1-9, 2015.
3. R. Girshick, J. Donahue, T. Darrell and J. Malik, "Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation," IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 580-587, 2014