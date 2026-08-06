from pydantic import BaseModel, ConfigDict


class Study(BaseModel):
    study_hour : int

    model_config = ConfigDict(
        json_schema_extra={
            "examples" : [
                {"study_hour" : 5}
            ]
        }
    )

