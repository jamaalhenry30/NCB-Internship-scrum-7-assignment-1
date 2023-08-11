from app import app
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')




# Product List
products = [
    {
        'id': 1,
        'title': 'Mercedes Benz G63',
        'image': 'benz.jpg',
        'price': 1000000.99,
        'description': 'This is a Mercedes Benz.'
    },
    {
        'id': 2,
        'title': 'Playstation 5',
        'image': 'ps5.jpg',
        'price': 290000.99,
        'description': 'This is a Playstation 5.'
    },
    {
        'id': 3,
        'title': 'A Bachelor of Science Degree',
        'image': 'bsc.jpg',
        'price': 0.99,
        'description': 'Do you want a decent job? Here you go.'
    },
    {
        'id': 4,
        'title': 'A virtuous woman',
        'image': 'girl.jpg',
        'price': '100000000000000000',
        'description': 'A virtuous woman is hard to find.'
    }
]

@app.route('/products')
def display_products():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def display_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_details.html', product=product)
    else:
        return "Product not found."

if __name__ == '__main__':
    app.run(debug=True)

