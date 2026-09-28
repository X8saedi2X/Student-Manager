class Student:
    def __init__(self,id:int,name:str,score:int):
        self.id = id
        self.name = name
        self.score = score


    def to_dict(self):
        return {
            "id" : self.id ,
            "name" : self.name ,
            "score" : self.score
        }

    @classmethod
    def from_dict(cls,data):
        return cls(
            data["id"],
            data["name"],
            data["score"]
        )


    @staticmethod
    def is_validate_score(score):
        return 0<= score <= 20


    @property
    def score(self):
        return self._score


    @score.setter
    def score(self,value):
        if Student.is_validate_score(value):
            self._score = value
        else:
            raise ValueError("Score must be between 0 and 20")