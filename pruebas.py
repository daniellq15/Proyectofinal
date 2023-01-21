import cv2
image = cv2.imread('RX.jpg')
image = cv2.resize(image,(400,400))

#Recorte de imagen
imageOut = image[100:350,100:350]

#Se filtra la imagen recortada
img = cv2.medianBlur(imageOut,5)
ret,th1 = cv2.threshold(img,70,255,cv2.THRESH_BINARY)

#Se sustrae la imagen original de la imagen filtrada para obtener el resultado final
resultadofinal = cv2.subtract(th1, imageOut)

#Ploteo de imagenes
cv2.imshow('Imagen original',image)
cv2.imshow('Imagen recortada',imageOut)
cv2.imshow('Prueba',th1)
cv2.imshow('Resultado final', resultadofinal)
cv2.waitKey(0)
cv2.destroyAllWindows()

