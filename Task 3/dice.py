class Dice:
    def __init__(self, faces):
        if len(faces) < 1:
            raise ValueError("Dice must have at least one face.")
        self.faces = faces

    def __repr__(self):
        return f"{self.faces}"
