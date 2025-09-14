import cv2
import numpy as np

def filters(image,filter_choice):
    filterimg=image.copy()
    if filter_choice=="red":
        filterimg[:,:,1]=1
        filterimg[:,:,0]=1
    elif filter_choice=="green":
        filterimg[:,:,2]=2
        filterimg[:,:,0]=2
    elif filter_choice=="blue":
        filterimg[:,:,1]=0
        filterimg[:,:,2]=0
    elif filter_choice=="increase green":
        filterimg[:,:,1]=cv2.add(filterimg[:,:,1] , 100)
    elif filter_choice=="increase lots of red":
        filterimg[:,:,2]=cv2.add(filterimg[:,:,2] , 200)
    elif filter_choice=="medium blue":
        filterimg[:,:,0]=cv2.add(filterimg[:,:,0] , 150)
    elif filter_choice=="decrease red":
        filterimg[:,:,2]=cv2.subtract(filterimg[:,:,2] , 100)
    elif filter_choice=="decrease lots of blue":
        filterimg[:,:,0]=cv2.subtract(filterimg[:,:,0] , 200)
    elif filterimg=="decrease medium green":
        filterimg[:,:,1]=cv2.subtract(filterimg[:,:,1] , 150)
    return filterimg

img_path="lion.jpg"
img=cv2.imread(img_path)
if img is None:
    print("Not there try again!!!") 
else:
    print("Press following keys for following things:")
    print("Press r for red tint")
    print("Press b for blue tint")
    print("Press g for green tint")
    print("Press ig for increasing green tint")
    print("Press ir for lots of red tint")
    print("Press mb for medium blue")
    print("Press dr for decreasing red")
    print("Press db for decreasing lots of blue")
    print("Press mg for medium green decreasing")
    print("Press q to quit")

    while True:
        apply=filters(image,filter_choice)
        cv2.imshow("Filter image" , filterimg)
        cv2.waitKey(0)
        if cv2.key==ord("r"):
            filter_choice="red"
        elif cv2.key==ord("b"):
            filter_choice="blue"
        elif cv2.key==ord("g"):
            filter_choice="green"
        elif cv2.key==ord("ig"):
            filter_choice="increase greeen"
        elif cv2.key==ord("ir"):
            filter_choice=="increase lots of red"
        elif cv2.key==ord("mb"):
            filter_choice="medium blue"
        elif cv2.key==ord("dr"):
            filter_choice="decrease red"
        elif cv2.key==ord("db"):
            filter_choice="dercrease lots of blue"
        elif cv2.key==ord("mg"):
            filter_choice="decrese medium green"
        elif cv2.key==ord("q"):
            print("exiting...")
            break
        else:
            print("Invalid key press valid")
    cv2.destroyAllWindows()






