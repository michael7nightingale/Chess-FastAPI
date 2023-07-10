from starlette.authentication import BaseUser


class FastAPIUser(BaseUser):
    def __init__(
            self,
            username: str | None = None,
            email: str | None = None,
            first_name: str | None = None,
            last_name: str | None = None,
            id: str | int | None = None,
            *args,
            **kwargs
    ):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

        self.data = {
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "id": self.id,

        }
        self.data.update(**kwargs)

    @property
    def identity(self) -> str:
        return self.id

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def display_name(self) -> str:
        return self.username
