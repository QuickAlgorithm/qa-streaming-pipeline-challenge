from pydantic import BaseModel, ConfigDict


class ResultSchema(BaseModel):
    id: int
    competence: float
    network_ability: float
    promoted: bool

    model_config = ConfigDict(from_attributes=True)
