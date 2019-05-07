from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") ## establish a root route /, which will render the template.html file, you can pass in other arguments int this fn
def template_test():
  return render_template('template.html', my_string='lubbadubba', my_list=[0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)