from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Flask!"


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def list_items():
    # Load items from the JSON file
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_data = data.get('items', [])

    return render_template('items.html', items=items_data)


@app.route('/product')
def product():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found")
        except json.JSONDecodeError:
            return render_template('product_display.html', error="Invalid JSON format")
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products = list(reader)
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found")
        except Exception as e:
            return render_template('product_display.html', error=f"Error reading CSV: {str(e)}")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            product = next((p for p in products if p.get('id') == str(product_id)), None)
            if product:
                return render_template('product_display.html', product=product)
            else:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")
    else:
        return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
