""" App food.

"""
from flask import Flask, render_template, request
from models import storage
from models.model_food import food

app = Flask(__name__)

@app.route('/food', strict_slashes=False, methods=['GET', 'POST'])
def app_food():
    """ This function displays a form of food items to store
    the name and value of each food item, with GET and POST methods.

    """
    if request.method == 'GET':
        return render_template('food.html')
    if request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        my_dict = {
            'id': 0,
            'name': name,
            'value': value
        }
        inst = food(**my_dict)
        storage.new_obj(inst)
        storage.save()
        return render_template('food.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)