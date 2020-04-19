import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_TRIPLEX


def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(frame)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', str(obj.data), '\n')

        if str(obj.type) == 'QRCODE':
        # print("Data", obj.data)
            cv2.putText(frame, (str('QRcode: ') + str(obj.data)[2:len(str(obj.data))-1]), (5, 50), font, 1, (0, 0, 255), 1)
        else:
            cv2.putText(frame, (str('Barcode: ') + str(obj.data)[2:len(str(obj.data)) - 1]), (5, 50), font, 1, (0, 0, 255), 1)
    return decodedObjects



# Display barcode and QR code location
def display(frame, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(frame, hull[j], hull[(j + 1) % n], (170, 255, 30), 3)


while True:
    _, frame = cap.read()

    decodedObjects = decode(frame)

    display(frame, decodedObjects)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break