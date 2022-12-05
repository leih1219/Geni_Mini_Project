from flask import Flask
from flask import request, render_template
import asyncio
import time
from werkzeug.utils import secure_filename
from image_recognition import Img_reco as IR

app = Flask(__name__)

# curr_loop = asyncio.get_running_loop()
prediction = []


@app.route('/predict', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        file = request.files['img']
        print('file_name:' + file.name)
        file.save(secure_filename(file.filename))
        start_time = time.time()
        try:
            output = IR().predict(secure_filename(file.filename))
            output.append(["Time spent", "\nProcessing time: {:.3f}s".format(time.time() - start_time)])
            return render_template('result.html', output=output)
        except:
            return render_template('result.html', output=["Invalid image!"])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
