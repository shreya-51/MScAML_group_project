from utils.models.model import *
from src.python.load_data import load_spectrograms
from sklearn.model_selection import train_test_split
from src.python.convert_to_c import convert_tf_model

img_path = "./utils/data/img"
random_state = 1
num_classes = 10
epochs = 100
batch_size = 32

X, y = load_spectrograms(img_path, size=(32, 32))
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=random_state)
input_shape = X_train[0].shape
model = get_img_model(input_shape, num_classes)
model.summary()
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1)
score = model.evaluate(X_test, y_test)
print(f"Test loss: {score[0]}")
print(f"Test accuracy: {score[1]}")

convert_tf_model(model)
