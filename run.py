from app import create_app

# import atexit
# from app.v1.config.thread_config import POOL_TIME, fetch


# run
if __name__ == '__main__':
    flask_app = create_app()


    # debug=False to run background process
    # flask_app.run(port=80, debug=False)

    flask_app.run(port=80, debug=True)