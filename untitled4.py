# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:39:38 2021

@author: Global Computers
"""

import cv2
camera = "http://10.107.3.15:8080//video"
cap = cv2.VideoCapture(0)

print("check==",cap.isOpened())


while True:
    ret, frame == cap.read()
    if ret ==True:
        cv2.imshow("color frame",frame)
        if cv2.waitKey(1) == 27:
            break

cap.destroyAllWindows()