from config import app
from backend.crud.users.usersBP import usersBP
from backend.crud.albums.albumsBP import albumsBP
from backend.crud.reviews.reviewsBP import reviewsBP
from frontend.frontendBP import frontendBP

app.register_blueprint(usersBP, url_prefix="/users")
app.register_blueprint(albumsBP, url_prefix="/albums")
app.register_blueprint(reviewsBP, url_prefix="/reviews")
app.register_blueprint(frontendBP, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)