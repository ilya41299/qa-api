from pydantic import BaseModel


class CommentScheme(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class PhotoScheme(BaseModel):
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str


class AlbumScheme(BaseModel):
    userId: int
    id: int
    title: str


class TodosScheme(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


class PostsScheme(BaseModel):
    userId: int
    id: int
    title: str
    body: str
