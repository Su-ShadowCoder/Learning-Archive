from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
print(__name__)

#base_page
@app.route("/")
def my_home():
    return render_template("index.html")

#relative_paths
@app.route("/<string:page_name>/")
def html_page(page_name):
    return render_template(page_name)




#submit_form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html/')
    else:
        return "something went wrong. Try again!"


