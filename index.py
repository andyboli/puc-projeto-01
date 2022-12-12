from view.app import run_view
from controller.orchestrator import restart_app


if __name__ == "__main__":
    try:
        run_view()
    finally:
        while True:
            try:
                success, loading, error = next(restart_app)
                if loading:
                    print(loading)
                elif success:
                    print(success)
                elif error:
                    print(error)
            except StopIteration:
                break
