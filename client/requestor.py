import requests
from qt_tools import show_exit_dialog
from functools import wraps


class Requestor:
    """
    Mixin for sending requests to the server from the main window to save logic here.
    """
    def __init__(self, check_token_func, main_window):
        self.main_window = main_window
        self.check_token_func = check_token_func

    @staticmethod
    def request_authorized(func):
        @wraps(func)
        def inner(self, url: str, window=None, status_code: int = 200, **kwargs):
            if window is None:
                window = self
            self.main_window.check_token()
            try:
                headers = {"Authorization": f"Bearer {self.main_window.config['token']}"}
                response = func(
                    self=self,
                    url=url,
                    headers=headers,
                    **kwargs
                )
                assert response.status_code == status_code
                return response
            except AssertionError:
                show_exit_dialog(window, "Data is invalid.")
            except requests.ConnectionError:
                show_exit_dialog(window, "Cannot connect to the server.")

        return inner

    @request_authorized
    def get_authorized(self, url: str, **kwargs):
        return requests.get(url=url, **kwargs)

    @request_authorized
    def post_authorized(self, url: str, json: dict | None = None, **kwargs):
        return requests.post(url=url, json=json, **kwargs)

    @staticmethod
    def request_unauthorized(func):
        @wraps(func)
        def inner(self, url: str, window=None, status_code: int = 200, **kwargs):
            if window is None:
                window = self
            try:
                response = func(
                    self=self,
                    url=url,
                    **kwargs
                )
                assert response.status_code == status_code
                return response
            except AssertionError:
                show_exit_dialog(window, "Something went wrong with your request.")
            except requests.ConnectionError:
                show_exit_dialog(window, "Cannot connect to the server.")
        return inner

    @request_unauthorized
    def get_unauthorized(self, url: str, **kwargs):
        return requests.get(url=url, **kwargs)

    @request_unauthorized
    def post_unauthorized(self, url: str, json: dict | None = None, **kwargs):
        return requests.post(url=url, json=json, **kwargs)

    def check_connection(self, window=None) -> None:
        """Check connection to the internet."""
        if window is None:
            window = self.main_window
        try:
            response = requests.get("https://example.com")
            assert response.status_code == 200
        except requests.ConnectionError:
            show_exit_dialog(window, "Bad internet connection")
        except Exception as e:
            show_exit_dialog(window, f"Unexpected error: {e}")
