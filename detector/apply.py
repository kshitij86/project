import tensorflow as tf
import cv2
import sys
CATEGORIES = ["fake", "real"]


def prepare(file):
    IMG_SIZE = 50
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("CNN.model")
# your image path
filename = sys.argv[1]
# Apply the model to any image.
try:
    image = f"C:/Users/Kshitij/Desktop/project/DATASET/real_and_fake_face/training_fake/{filename}"
    """
    The following modified image is "real". :/
    alt_path = f"C:/Users/Kshitij/Desktop/project/xy.jpg"
    """
    prediction = model.predict([prepare(image)])
    prediction = list(prediction[0])
    print(CATEGORIES[prediction.index(max(prediction))])
except Exception as e:
    print(f"An error occured : {e}.")
