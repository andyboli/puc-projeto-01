from view.app import run_view
from controller.orchestrator import end_app


if __name__ == "__main__":
    try:
        run_view()
    finally:
        while True:
            try:
                message, error = next(end_app)
                if message:
                    print(message)
                if error:
                    print(error)
            except StopIteration:
                break
