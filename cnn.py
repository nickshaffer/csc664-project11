import torch
# print(torch.cuda.is_available())
from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image, plot_prediction_grid
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
import os
import random

val = input("Enter 1 to train, 2 to predict a image, or 3 to quit: ")
while(val != "3"):
    if(val == "1"):
        custom_transforms = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize(900),
        # transforms.Resize(256),
        transforms.RandomHorizontalFlip(0.5),
        transforms.ColorJitter(saturation=0.2),
        transforms.ToTensor(),
        utils.normalize_transform(),
        ])

        Train_dataset=core.Dataset('Train/',transform=custom_transforms)
        Test_dataset = core.Dataset('Test/')
        loader=core.DataLoader(Train_dataset, batch_size=4, shuffle=True)
        model = core.Model(['TBbacillus'])

        torch_model = model.get_internal_model()
        print(type(torch_model))

        # --- improvement attempts ---

        # --- improvement attempt: 1 ---
        # for name, p in torch_model.named_parameters():
        #     print(name, p.requires_grad)

        #     if 'roi_heads' not in name and 'rpn' not in name:
        #         p.requires_grad = False

        losses = model.fit(loader, Test_dataset, epochs=10, lr_step_size=5, learning_rate=0.01, verbose=True)

        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.plot(losses)
        plt.show()

        model.save('model_weights.pth')
    if(val == "2"):
        model = core.Model.load('model_weights.pth', ['TBbacillus'])

        res = input("Enter 1 for images from kaggle with TB, 2 for images from kaggle without TB,\n\t3 for images that are from the internet, and 4 for your own images: ")
        folder = "images - kaggle with TB"
        match int(res):
            case 1:
                folder = "images - kaggle with TB"
            case 2:
                folder = "images - kaggle without TB"
            case 3:
                folder = "images - internet"
            case 4: 
                folder = "images - your own"

        if len(os.listdir(folder)) == 0:
            print("Folder is empty!")

        else:    
            for filename in os.listdir(folder):
                if val == "3":
                    break
                if filename.endswith('.jpg'):
                    image = utils.read_image(folder + '/' + filename) 
                    predictions = model.predict(image)
                    labels, boxes, scores = predictions
                    # show_labeled_image(image, boxes, labels)

                    thresh=.5
                    filtered_indices=np.where(scores>thresh)
                    filtered_scores=scores[filtered_indices]
                    filtered_boxes=boxes[filtered_indices]
                    num_list = filtered_indices[0].tolist()
                    filtered_labels = [labels[i] for i in num_list]
                    show_labeled_image(image, filtered_boxes, filtered_labels)
                    val = input("Enter 2 to predict the next image or 3 to exit predicting: ")

    val = input("Enter 1 to train, 2 to predict, or 3 to quit: ")

print("closing program...")

