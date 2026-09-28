class Student:
    def __init__(self,id:int,name:str,score:float):
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

# ================================
# validation for score
# ================================
    @staticmethod
    def is_validate_score(score):
        return 0<= score <= 20

    @staticmethod
    def has_max_two_decimals(value):
        return round(value,2) == value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if Student.is_validate_score(value) and Student.has_max_two_decimals(value):
            self._score = value
        else:
            raise ValueError("Score must be between 0 and 20 and have at most 2 decimal places")


# ================================
# validation for name
# ================================

    @staticmethod
    def is_validate_name(name):
        return 0 < len(name) <= 50

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if Student.is_validate_name(value):
            self._name = value
        else:
            raise ValueError("Name must be less than 50 character")




