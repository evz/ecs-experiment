from app.database import db
from app import models
from app import create_app

if __name__ == "__main__":
    fake_app = create_app()

    with fake_app.test_request_context():

        db.create_all()
