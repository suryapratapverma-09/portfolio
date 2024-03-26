from flask import Flask,render_template


app=Flask(__name__,template_folder="template")

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contacts():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__=="__main__":
    app.run(debug=True)

