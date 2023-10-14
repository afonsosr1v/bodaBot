from flask import render_template
#from flask_bootstrap import Bootstrap5

import config
from models import User


app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

#bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    users = User.query.all()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)