import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os
from classifier import ImageClassifier

class LetterIdentifierGUI:
    def __init__(self, classifier, master):
        self.classifier = classifier
        self.master = master
        self.master.title("Letter Identifier")

        self.camera = cv2.VideoCapture(0)
        self.camera_width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.camera_height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.canvas = tk.Canvas(self.master, width=self.camera_width, height=self.camera_height)
        self.canvas.pack()

        self.prediction_label = tk.Label(self.master, text="Prediction: ")
        self.prediction_label.pack()

        self.update()

    def update(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            image = ImageTk.PhotoImage(image=image)

            self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
            self.canvas.image = image

            predicted_letter = self.classify_frame(frame)
            self.prediction_label.config(text="Prediction: " + predicted_letter)

        self.master.after(10, self.update)

    def classify_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        resized = cv2.resize(gray, (128, 128))
        flattened = resized.flatten()
        predicted_label = self.classifier.model.predict([flattened])[0]
        return os.path.basename(predicted_label)

def main():
    image_folders = [ 
                     "E:\OneDrive\Music\pqrst\SMALLT","E:\OneDrive\Music\pqrst\SMALLR","E:\OneDrive\Music\pqrst\s","E:\OneDrive\Music\pqrst\q","E:\OneDrive\Music\pqrst\p"]
    classifier = ImageClassifier(image_folders)
    classifier.load_images()
    classifier.train_test_split()
    classifier.train_model()

    root = tk.Tk()
    app = LetterIdentifierGUI(classifier, root)
    root.mainloop()

if __name__ == "__main__":
    main()
