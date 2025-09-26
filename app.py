
from flask import Flask, render_template, send_from_directory
import math  # ✅ Import math module

app = Flask(__name__)

# ✅ Add missing routes
@app.route('/')
def index():
    return render_template("index.html", math=math, segment = 'home')

@app.route('/about')
def about():
    return render_template('about.html', math=math, segment = 'about')

@app.route('/contact')
def contact():
    return render_template('contact.html',math=math, segment = 'contact')

@app.route('/services')
def services():
    return render_template('services.html',math=math, segment = 'services')

@app.route('/foreign-remittance')
def foreign():
    return render_template('foreign-remittance.html',math=math, segment = 'services')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html', math=math , segment = 'pricing')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', math=math)

@app.route('/refund')
def refund():
    return render_template('refund.html', math=math)

@app.route('/terms')
def terms():
    return render_template('terms.html', math=math)


# blog

@app.route('/blog')
def blog():
    return render_template('blog.html',math=math, segment = 'blog')

@app.route('/benefits-of-upi-for-small-businesses')
def blog1():
    return render_template('blogs/benefits-of-upi-for-small-businesses.html',math=math, segment = 'blog')

@app.route('/why-indian-businesses-trust-upi-and-you-should-too')
def blog2():
    return render_template('blogs/blog-2.html',math=math, segment = 'blog')

@app.route('/international-collection')
def blog3():
    return render_template('blogs/blog-3.html',math=math, segment = 'blog')


@app.route('/collection-services-ecommerce-0-95-gst')
def blog4():
    return render_template('blogs/blog-4.html',math=math, segment = 'blog')











@app.route('/sitemap.xml')
def site1():
    return render_template('sitemap.xml'), 200, {'Content-Type': 'application/xml'}

@app.route('/feed.xml')
def site2():
    return render_template('feed.xml'), 200, {'Content-Type': 'application/xml'}

@app.route('/comments.xml')
def site3():
    return render_template('comments.xml'), 200, {'Content-Type': 'application/xml'}




# end

@app.route('/404')
def page_not_found():
    return render_template('404.html')

# Run the Flask app
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", debug=True)

