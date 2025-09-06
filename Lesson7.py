import cv2

#Image1 resizing
image1=cv2.imread("images.jpg")
cv2.namedWindow("screen" , cv2.WINDOW_NORMAL )
cv2.resizeWindow("screen",500,500)
cv2.imshow("screen" , image1)

#image2 resizing
image2=cv2.imread("lion.jpg")
#resizing image without window
cv2.namedWindow("screen" , cv2.WINDOW_NORMAL)
cv2.resizeWindow("screen",300,400)
cv2.imshow("screen" , image2)

#image3 
image3= cv2.imread("Tigre.jpg")
cv2.namedWindow("screen" , cv2.WINDOW_NORMAL)
cv2.resizeWindow("screen" , 300 , 300)
cv2.imshow("screen" , image3)



cv2.waitKey(0)
cv2.destroyAllWindows()

#This code is wrong , just tell me the changes so i will resubmit it after editing

