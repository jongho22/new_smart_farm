from flask import *
from flask_pymongo import PyMongo
from datetime import datetime

web_gui = Flask(__name__)
web_gui.config["MONGO_URI"] ="mongodb://localhost:27017/webgui_project"
mongo = PyMongo(web_gui)

@web_gui.route("/data_send", methods = ["GET", "POST"])
def collect_data():
    if request.method == "POST":
        raw_data0 = request.form.get("raw_data0")
        current_utc = round(datetime.utcnow().timestamp()*1000)
        print(raw_data0)
        print(current_utc)

        data = mongo.db.board
        post = {
            "raw_data0": raw_data0,
            "utc_stamp": current_utc,
        }

        data.insert_one(post)

        return ""
    else :
        return render_template("data_send.html")



if __name__ == "__main__" :
    web_gui.run(debug=True,port=9999)