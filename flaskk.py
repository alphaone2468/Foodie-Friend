from flask import Flask, render_template,request
import test
 
app = Flask(__name__)
 
 

@app.route("/",methods=['POST','GET'])
def food():
    if request.method=='POST':
        print("in if")
        user=request.form['rest']
        user1=request.form['restname']
        print(user)
        print(user1)
        price= test.get_data(user)
        price1=test.get_data2(user)
        print(price)
        print(price1)
        di=[{
            "swiggy": price,
            "zomato" : price1
        }]
        return render_template("food.html",list=di)
    else:
        print("i am in else")
        return render_template("food.html")
 
if __name__ == "__main__":
    app.run()