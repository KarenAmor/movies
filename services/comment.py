from models.comment import Comment as CommentModel
from schemas.comment import Comment

class CommentService:

    def __init__(self, db) -> None:
        self.db = db
    
    def get_comment(self, id_movie):
        result = self.db.query(CommentModel).filter(CommentModel.id_movie == id_movie).first()
        return result

    def create_comment(self, comment: Comment):
        new_comment = CommentModel(**comment.dict())
        self.db.add(new_comment)
        self.db.commit()
        return new_comment