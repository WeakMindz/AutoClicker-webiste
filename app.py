from flask import Flask ,render_template,send_from_directory



app = Flask(__name__) 



@app.route('/')
def home():
    return render_template("home.html")



@app.route('/download')
def download():
    return send_from_directory('static', 'main.py', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)