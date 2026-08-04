from pydantic import BaseModel, ConfigDict

class Book(BaseModel):
    id : int
    title : str
    price : int
    isbn : int

    model_config = ConfigDict(
        json_schema_extra={
            "examples" : [
                {
                    "id" : 1,
                    "title" : "FastAPI",
                    "price" : 20000,
                    "isbn" : 1234
                }
            ]
        }
    )

# class BookInfo(BaseModel):
#     title : str
#     price : int
#     isbn : int

#     model_config = ConfigDict(
#         json_schema_extra={
#             "examples" : [
#                 {
#                     "title" : "FastAPI",
#                     "price" : 20000,
#                     "isbn" : 1234
#                 }
#             ]
#         }
#     )