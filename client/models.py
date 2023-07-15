from pydantic import BaseModel


class Move(BaseModel):
    from_id: str
    to_id: str
    from_data: str
    to_data: str
    move_user: str
    move_color: str
    new_color: str
