from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password  # Note: In production, don’t expose raw passwords
        }

    @staticmethod
    def from_row(row):
        if row is None:
            return None
        return User(id=row[0], name=row[1], email=row[2], password=row[3])

