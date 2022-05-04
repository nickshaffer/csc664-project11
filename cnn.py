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
        transforms.RandomHorizontalFlip(0.5),
        transforms.ColorJitter(saturation=0.2),
        transforms.ToTensor(),
        utils.normalize_transform(),
        ])

        Train_dataset=core.Dataset('Train/',transform=custom_transforms)#L1
        Test_dataset = core.Dataset('Test/')#L2
        loader=core.DataLoader(Train_dataset, batch_size=2, shuffle=True)#L3
        model = core.Model(['TBbacillus'])#L4
        losses = model.fit(loader, Test_dataset, epochs=25, lr_step_size=5, learning_rate=0.001, verbose=True)#L5

        plt.plot(losses)
        plt.show()

        model.save('model_weights.pth')
    if(val == "2"):
        model = core.Model.load('model_weights.pth', ['TBbacillus'])

        for filename in os.listdir('Images'):
            if val == "3":
                break
            if filename.endswith('.jpg'):
                image = utils.read_image('Images/' + filename) 
                predictions = model.predict(image)
                labels, boxes, scores = predictions
                # show_labeled_image(image, boxes, labels)

                thresh=0.4
                filtered_indices=np.where(scores>thresh)
                filtered_scores=scores[filtered_indices]
                filtered_boxes=boxes[filtered_indices]
                num_list = filtered_indices[0].tolist()
                filtered_labels = [labels[i] for i in num_list]
                show_labeled_image(image, filtered_boxes, filtered_labels)
                val = input("Enter 2 to predict the next image or 3 to exit predicting: ")

    val = input("Enter 1 to train, 2 to predict, or 3 to quit: ")

print("closing program...")

