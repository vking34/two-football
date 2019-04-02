from app import create_app
# from flask_bcrypt import Bcrypt

#run
if __name__ == '__main__':
    app = create_app()
    app.run(port=80, debug=True)
