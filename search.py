import cv2
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)

credentials = ApiKeyCredentials(in_headers={"Prediction-key": "<Prediction-key>"})
predictor = CustomVisionPredictionClient("<Endpoint-URL>", credentials)

camera.capture('/home/pi/flask/capture_search.png')
image = cv2.imread('capture_search.png')
cv2.imwrite('capture_search.png', image)

with open("capture_search.png", mode="rb") as captured_image:
    results = predictor.detect_image("<Project-id>", "<Name-of-iteration", captured_image)

for prediction in results.predictions:
    if prediction.probability > 0.4 :

        bbox = prediction.bounding_box

        cv2.putText(image, prediction.tag_name, (int(bbox.left * 640), int(bbox.top * 480)-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        result_image = cv2.rectangle(image, (int(bbox.left * 640), int(bbox.top * 480)), (int((bbox.left + bbox.width) * 640), int((bbox.top + bbox.height) * 480)), (0, 255, 0), 1)
        cv2.imwrite('result_search.png', result_image)


camera.close()
