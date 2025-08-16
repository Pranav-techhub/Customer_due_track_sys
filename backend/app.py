from flask import Flask
from routes import customer_bp

def create_app():
    app = Flask(__name__)

    # Register routes
    app.register_blueprint(customer_bp, url_prefix="/")

    @app.route("/", methods=["GET"])
    def home():
        return {"message": "Backend is running!"}, 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
