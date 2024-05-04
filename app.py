from flask import Flask ,render_template,redirect,url_for,request
app=Flask(__name__)
@app.route("/")
def home_page():
  return render_template('home.html')

@app.route("/login", methods=['GET','POST'])
def login_page():
  
  if request.method=='POST':
    user=request.form['nm']
    return redirect(url_for("user", usr=user))
    


  else:
    return render_template("login.html")


@app.route("/<usr>")
def user(usr):
  return f"{usr}"
    
if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)