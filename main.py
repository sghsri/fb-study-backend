from app import app
from routes.meta_routes import meta_routes
from routes.job_routes import job_routes

app.register_blueprint(meta_routes)
app.register_blueprint(job_routes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
