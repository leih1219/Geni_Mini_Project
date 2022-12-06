from flask import Flask
from flask import request, render_template
import time
from werkzeug.utils import secure_filename
from image_recognition import Img_reco as IR

app = Flask(__name__)

prediction = []


@app.route('/predict', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        file = request.files['image']
        print('file_name:' + file.name)
        file.save(secure_filename(file.filename))
        start_time = time.time()
        output = IR().predict(secure_filename(file.filename))
        context = {
            'key1': output[0][0],
            'value1': output[0][1],
            'key2': output[1][0],
            'value2': output[1][1],
            'key3': output[2][0],
            'value3': output[2][1],
            'key4': output[3][0],
            'value4': output[3][1],
            'key5': output[4][0],
            'value5': output[4][1],
            'time': time.time() - start_time
        }
        return render_template('result.html', **context)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
