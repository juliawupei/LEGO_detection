import cv2
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

credentials = ApiKeyCredentials(in_headers={"Prediction-key": "<Prediction-key>"})
predictor = CustomVisionPredictionClient("<Endpoint-URL>", credentials)

ret, image = camera.read()
cv2.imwrite('capture_detect.png', image)

with open("capture_detect.png", mode="rb") as captured_image:
    results = predictor.detect_image("<Project-id>", "<Name-of-Iteration>", captured_image)

for prediction in results.predictions:
    if prediction.probability > 0.5 :

        bbox = prediction.bounding_box
        cv2.putText(image, prediction.tag_name, (int(bbox.left * 640), int(bbox.top * 480)-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        result_image = cv2.rectangle(image, (int(bbox.left * 640), int(bbox.top * 480)), (int((bbox.left + bbox.width) * 640), int((bbox.top + bbox.height) * 480)), (0, 255, 0), 1)
        cv2.imwrite('result_detect.png', result_image)
        print (prediction.tag_name)

camera.release()      
return prediction.tag_name
