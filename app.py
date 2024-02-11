from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from braintumorClassifier.utils.common import decodeImage
from braintumorClassifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
@cross_origin()
# def predictRoute():
    # try:
    #     if 'image' not in request.files:
    #         return jsonify({'error': 'No file part'}), 500
    #     file = request.files['image']

    #     if file.filename == '':
    #         return jsonify({'error': 'No selected file'}), 500
        
    #     if file:
    #         filepath = os.path.join('/tmp',  'uploaded_image.jpg')
    #         file.save(filepath)

    #         result = clApp.predict(filepath)
    #         return jsonify(result)
    # except Exception as e:
    #     app.logger.error(f'Unexpected error: {e}')

    #     return jsonify({'error': str(e)}), 500
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

    
  


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=70, debug=True) #local host
    # app.run(host='0.0.0.s0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=8080) #for AZURE