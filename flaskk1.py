from flask import Flask, render_template,request
import test
 
app = Flask(__name__)
 
 

@app.route("/",methods=['POST','GET'])
def food():
    if request.method=='POST':
        print("in if")
        restN=request.form['restname']
        print(restN)
        if(restN=='paradise'):
            price1='swiggy price'
            price2='zomato price'
            menu='menu'
            list=[price1,price2,menu]
            print(list)
        return render_template("details.html",value=list)
    else:
        print("i am in else")
        return render_template("food1.html")
 
if __name__ == "__main__":
    app.run()