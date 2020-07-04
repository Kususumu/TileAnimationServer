import cv2

# get tge picture
img = cv2.imread("C:\\Users\\DELL\\Desktop\\aracimage\\man.png")

# create and render
cv2.namedWindow("Image")
cv2.imshow("Image",img)
cv2.waitKey(0)

# Release the window
cv2.destroyAllWindows()