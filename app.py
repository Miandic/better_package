from flask import Flask, render_template, url_for, request
import Parser.main
import json
#print("Setting 'recieved_data' to placeholder stats")
recived_data = [0, 1, 2, 3, 4, 5, 6]
#print("recived_data now is ", recived_data)

q = {
        "a": 0
}
with open("flag.json", "w") as write_file:
    json.dump(q, write_file)



app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    global recived_data
    #print("Entered 'Index' function with 'recived_data' on ", *send_data())
    if request.method == 'POST':
        city_from = request.form['city1']
        city_to = request.form['city2']
        length = request.form['length']
        width = request.form['width']
        high = request.form['high']
        weight = request.form['weight']
        cost = request.form['cost']
        recived_data = [city_from, city_to, length, width, high, weight, cost]
        #print("Updated 'recived_data' to: ", *send_data(), " and importing 'Parser.main' file")
        #print("Just imported 'Parser.main file with 'recived_data' on: ", *send_data())
        parsed_data = Parser.main.parse(send_data())
        #print("just get this data: ", *parsed_data)
        try:
            return render_template('index.html', data=parsed_data)
        except:
            return "Error: please input all data"
    else:
        data = "Nothing was ever parced"
        return render_template('index.html', data=data)


def send_data():
    global recived_data
    #print("Entered 'send_data' function with 'recived_data' ", recived_data)
    return recived_data

#print("Line 40 processing, right now in 'recieved_data': ", send_data())


if __name__ == '__main__':
    app.run(debug=True)
