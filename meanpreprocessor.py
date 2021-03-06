# import lib
import cv2

class MeanPreprocessor:
	def __init__(self, rMean, gMean, bMean):
		# store the RGB channel average cross a training set
		self.rMean = rMean
		self.gMean = gMean
		self.bMean = bMean

	def preprocess(self, image):
		# split the image into its respective RGB channels
		(B, G, R) = cv2.split(image.astype("float32"))
		
		# subtract the means for each channel
		R -= self.rMean
		G -= self.gMean
		B -= self.bMean
	
		# merge 
		return cv2.merge([B, G, R])
