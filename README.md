The layout of the project is simple and each file serves a specific function. The 
train.py file was used to train the model using the data in the squares folder. On 
the other hand, the test.py file was used to test the accuracy of the model which is
saved as model2.h5. The divide.py file does all the image processing required to 
detect the lines to divide the board on and then divides it into sub-images. The 
predict.py file then uses the model to predict what pieces are in each sub-image. This
array of predictions is then passed onto translate.py which translates that data 
into an FEN string. The FEN string is then given to the evaluation.py file which 
gets the evaluation of the position through a call to the stockfish API. This is all
displayed in the GUI which is in the main.py file. 