from flask import Flask, render_template, url_for, reque
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        city_from = request.form['city1']
        city_to = request.form['city2']
        length = request.form['length']
        width = request.form['width']
        high = request.form['high']
        weight = request.form['weight']
        cost = request.form['cost']
        print("Debug: city_from -", city_from, "city_to -", city_to, "length -", length, "width -", width, "high -",
              high, "weight -", weight, "cost -", cost)

        try:
            return render_template('index.html', )
        except:
            return "Error: please input all data"
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
