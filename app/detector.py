import requests
def detect_item(image,key):
    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/0de016b9-0ed5-4edc-8611-7c0487198bfa/LabelFile/'
    data = {'file': open(image, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth(key, ''), files=data)
    return (response.text)