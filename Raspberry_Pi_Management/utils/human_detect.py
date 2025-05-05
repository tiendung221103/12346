import time
import cv2
from ultralytics import YOLO
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from utils.firebase import Firebase
import threading

firebase = Firebase()

class HumanDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.results = None

    def detect_humans(self, frame):
        self.results = self.model.predict(frame, classes=[0], conf=0.5)  # Class 0 is 'person'

    def draw_boxes(self, frame, results):
        annotated_frame = results[0].plot()
        return annotated_frame
    def set_data_to_firebase(self):
        while True:
            if self.results is not None:
                if len(self.results[0].boxes) > 0:  # Check if any detections exist
                    print("True")  # Human detected
                    firebase.set_data('/room/human', "true")
                else:
                    print("False")  # No human detected
                    firebase.set_data('/room/human', "false")
            else:
                print("No results to process.")
            time.sleep(2)
    def process_video(self, video_source=0):
        cap = cv2.VideoCapture(video_source)
        cap.set(3, 900)  # Set width
        cap.set(4, 600)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            self.detect_humans(frame)
            annotated_frame = self.draw_boxes(frame, self.results)
            cv2.imshow("Human Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    detector = HumanDetector()
    threading.Thread(target=detector.process_video).start()
    threading.Thread(target=detector.set_data_to_firebase).start()
