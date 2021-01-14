import cv2
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

credentials = ApiKeyCredentials(in_headers={"Prediction-key": "4a065daf45d9493481150079bcecedd9"})
predictor = CustomVisionPredictionClient("https://southcentralus.api.cognitive.microsoft.com/", credentials)

ret, image = camera.read()
cv2.imwrite('capture.png', image)

with open("capture.png", mode="rb") as captured_image:
    results = predictor.detect_image("1b347900-c97b-4769-88bf-266ebfa913b7", "Iteration7", captured_image)

for prediction in results.predictions:
    if prediction.probability > 0.5 and prediction.tag_name == "2_8":

        bbox = prediction.bounding_box

        cv2.putText(image, prediction.tag_name, (int(bbox.left * 640), int(bbox.top * 480)-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        result_image = cv2.rectangle(image, (int(bbox.left * 640), int(bbox.top * 480)), (int((bbox.left + bbox.width) * 640), int((bbox.top + bbox.height) * 480)), (0, 255, 0), 1)
        cv2.imwrite('result.png', result_image)


camera.release()