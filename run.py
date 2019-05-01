from app import create_app

# import atexit
# from app.v1.config.thread_config import POOL_TIME, fetch


# run
if __name__ == '__main__':
    app = create_app()


    # debug=False to run background process
    app.run(port=80, debug=False)

    # app.run(port=80, debug=True)