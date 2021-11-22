from flask import Flask, render_template, url_for, request

app = Flask(__name__)

recived_data = [0, 0, 0, 0, 0, 0, 0]

@app.route('/', methods=['POST', 'GET'])
def index():
    global recived_data
    if request.method == 'POST':
        city_from = request.form['city1']
        city_to = request.form['city2']
        length = request.form['length']
        width = request.form['width']
        high = request.form['high']
        weight = request.form['weight']
        cost = request.form['cost']
        recived_data = [city_from, city_to, length, width, high, weight, cost]
        print(send_data())
        import Parser.main
        parsed_data = Parser.main.parse()
        print(parsed_data)
        try:
            return render_template('index.html', data=parsed_data)
        except:
            return "Error: please input all data"
    else:
        data = [['name', 'cost', 'date'], ['name2', 'cost2', 'date2']]
        return render_template('index.html', data=data)


def send_data():
    return recived_data


if __name__ == '__main__':
    app.run(debug=True)
