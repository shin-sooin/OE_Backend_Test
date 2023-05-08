from flask import Flask, redirect, render_template, url_for
from DB_handler import DBModule
from model import Model
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

app = Flask(__name__)
app.secret_key = "wjddusdlek!!wjddusdlfkrn!!@"

DB = DBModule()
M = Model()

@app.route("/", methods={"POST", "GET"})
def index():
    path_dlocal, mode, uid, filename = DB.pull("Original/0/jyeon/IMG_3080.jpg")
    # path_dlocal, mode, uid, filename = DB.pull("Original/1/jyeon/IMG_3080.jpeg")
    path_ulocal = path_dlocal.replace("downloads", "uploads")
    info, summary, error = M.modeling(mode, path_dlocal, path_ulocal)
    DB.push(mode=mode, uid=uid, filename=filename, path_ulocal=path_ulocal, info=info, summary=summary, error=error)
    return render_template("base.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)