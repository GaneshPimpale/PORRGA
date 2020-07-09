from keras.applications.vgg19 import VGG19, decode_predictions, preprocess_input
from keras.preprocessing.image import img_to_array, load_img


class vgg19Test:

    def image_id(image):
        # load model
        model = VGG19()
        # load/resize/preprocess test image
        img = load_img(image, target_size=(224, 224))
        img = img_to_array(img)
        img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
        img = preprocess_input(img)
        # predict probabilities for each class
        yhat = model.predict(img)
        label = decode_predictions(yhat)
        # find the class with the highest probability and print out likelihood
        label = label[0][0]
        print(label[1] + ', ' + '%.2f' % (label[2] * 100) + '% likelihood')

    image_id('C:/Users/ehuan/Desktop/SHTEM/PORRGA/POR/testImages/TEST9.jpg')

