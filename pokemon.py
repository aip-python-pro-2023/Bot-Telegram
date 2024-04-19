class Pokemon:
    def __init__(self, id: int, name: str, height: float, weight: float):
        self._id = id
        self._name = name
        self._height = height
        self._weight = weight

    def __repr__(self):
        return f"Покемон(id={self._id}, Имя='{self._name}', Рост={self._height}, Вес={self._weight})"

class BasePokemon:
    def __init__(self, name: str):
        self._name = name

    def __repr__(self):
        return f"BasePokemon(name='{self._name}')"
