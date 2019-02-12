import cv2
import os
import imutils
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

# Input Image Importation
def image_loading(image_path):
    imgLoaded = []
    imgLoaded = os.listdir(image_path)
    return imgLoaded    

# Histogram
def Histogram(image_path, size):
    img = cv2.imread(image_path)
    b,g,r = cv2.split(img)    
    histBlue = cv2.calcHist([img],[0],None,[size],[0,size])
    histGreen = cv2.calcHist([img],[1],None,[size],[0,size])
    histRed = cv2.calcHist([img],[2],None,[size],[0,size])
    
    # Formalizing the histogram using imutils
    if imutils.is_cv2():
        histBlue = cv2.normalize(histBlue)
        histGreen = cv2.normalize(histGreen)
        histRed = cv2.normalize(histRed)
    else:
        cv2.normalize(histBlue, histBlue)
        cv2.normalize(histGreen, histGreen)
        cv2.normalize(histRed, histRed)

    histogramSum = histBlue + histGreen + histRed
    return histogramSum

# Distance 
def DistCol(image_requet, dataset_path, size, n=5):
    list_img = image_loading(dataset_path)
    histSum = 0   
    sub = 0
    trie = []
    hist1 = []
    hist2 = []
    subtraction = []
    dist = []
    hist1 = Histogram(image_requet, size)   
    
    # Input Image Vector Value
    for i in range (len(hist1)):
        histSum += hist1[i]
    
    # Dataset reading and difference bettween the vector values
    for i in range(len(list_img)):
        path = dataset_path + list_img[i]
        hist2 = Histogram(path, size)
        for j in range(len(hist2)):
            sub += abs(hist1[j] - hist2[j])
        # Putting the substraction value and the image name in a list
        concatSoubList = [sub] + [list_img[i]]  
        subtraction.append(concatSoubList)
        sub = 0
    
    # Distance and Results   
    for i in range(len(subtraction)):
        calDist = subtraction[i][0] / histSum   

        #get image name in sub list that containe substraction and the name  
        imgName = subtraction[i][1]  

        #concatenate Distance and image name 
        result = [calDist] + [imgName]     
        dist.append(result)

    # Distance Value sorting   
    sorting = sorted(dist)  
    
    print("==== Application Parameters  ==== ")             
    print("Image Request :", image_requet)
    print("image path to the base :", dataset_path)
    print("Histogram size :", size)
    print()
    for i in range(n):
        # Showing the results
        print(sorting[i])

    
    print()

    return dist

def SearchEngineImageApp():
    # Menu display variable
    menuDisplay = True
    while (menuDisplay):
        # Game Presentation
        print("\n***********************************************************")
        print("***** Welcome to the Elites Images Search Engine   ********")
        print("***** This program will give you 5 similar images  ********")
        print("***** Press number 1 to search for similar Images  ********")
        print("***** Press number 2 to Quit the Application now   ********")
        print("***** We're so happy to be your Fav Search Engine  ********")
        print("***********************************************************")
        
        # Random the number
        #Myresult = sample(range(1, 100), 3)
        
        # Get the user input
        choice = input()
        # Check the teh user input
        if (choice=="1"):
            searchEngineDatasetPath = "/home/jobee/Desktop/imageSearch/images/"   
            inputImgPath=input("Please give the image path including its extension: ")
            DistCol(inputImgPath, searchEngineDatasetPath, 32)
            break;

        if (choice=="2"):
            print("Thank You For Your Time, See You Soon On Elites Images Search Engine")
            menuDisplay = False


# Elites Images Search engine
if __name__ == "__main__":
    SearchEngineImageApp()
    
