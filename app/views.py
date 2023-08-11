
from app import app
import os
from flask import render_template, request, redirect, send_from_directory, url_for, flash, session, abort
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jamaal Henry")


# Product List
products_data = [
    {
        'id': 1,
        'title': 'Serene Chromatic Symphony',
        'image': 'img1.jpeg',
        'price': '455430.99',
        'description': "Experience the captivating world of Serene Chromatic Symphony, a masterpiece that transcends the ordinary and invites you to immerse yourself in a realm of colors, textures, and emotions. Created by a visionary artist, this painting is a celebration of artistic expression, where each brushstroke dances harmoniously to compose a symphony of serenity."
    },
    {
        'id': 2,
        'title': 'Crimson Dreamscape: Whispers of the Scarlet Forest',
        'image': 'img2.jpeg',
        'price': '54545.43',
        'description': 'Step into the enchanting world of "Crimson Dreamscape," a mesmerizing painting that beckons you to explore the mystical depths of the Scarlet Forest. Crafted by the deft hand of an imaginative artist, this masterpiece captures the essence of a realm where reality and fantasy entwine.'
    },
    {
        'id': 3,
        'title': 'Starry Reverie: Celestial Whispers in Midnight Hues',
        'image': 'img3.jpeg',
        'price': '43533.44',
        'description': 'Behold the mesmerizing canvas of "Starry Reverie," a captivating painting that invites you to lose yourself amidst a celestial dreamscape painted in the enchanting palette of midnight hues. The artists skilled hand weaves a tale of cosmic wonder, where stars twinkle like distant promises and galaxies unfold like chapters in a cosmic book.'
    },
    {
        'id': 4,
        'title': "Eternal Harmony: Fusion of Nature and Technology",
        'image': 'img4.jpeg',
        'price': '556423.22',
        'description': 'Enter the realm of "Eternal Harmony," a visionary painting that encapsulates the seamless convergence of nature and technology. With each brushstroke, the artist unveils a world where the organic and the mechanical intertwine, creating a mesmerizing symphony of balance and coexistence.'
    },
    {
        'id': 5,
        'title': "Whispers of Time: A Journey Through Ancient Echoes",
        'image': 'img5.jpeg',
        'price': '23354.56',
        'description': 'Embark on a captivating journey through the corridors of history with "Whispers of Time," a evocative painting that captures the essence of bygone eras and tales untold. The artist"s brush has breathed life into the canvas, inviting you to explore the intricate tapestry of human experiences that have shaped our world.'
    }
]

@app.route('/products')
def display_products():
    return render_template('products.html', products_data=products_data)

@app.route('/product/<int:product_id>')
def display_product(product_id):
    item = next((p for p in products_data if p['id'] == product_id), None)
    if item:
   
        return render_template('product_details.html', item=item)
    else:
        return "Product not found."
    
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
