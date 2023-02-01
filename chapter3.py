import cv2

image1 = cv2.imread("Image/lunar.jpg", cv2.IMREAD_ANYCOLOR)
if image1 is not None:
    cv2.imshow("IMG", image1)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("No image file.")

image2 = cv2.imread("Image/lunar.jpg", cv2.IMREAD_GRAYSCALE)
if image2 is not None:
    cv2.imshow("IMG", image2)
    cv2.imwrite("Image/lunar_gray.jpg", image2)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("No image file.")
