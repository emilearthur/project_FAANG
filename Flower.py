class Flower:
    """ A Flower """

    def __init__(self, name: str, num_petals: int, price: (int, float)) -> None:

        """
        Create a new flower instance.
        The initial balance is zero.

        name        the name of the flower (eg. 'Hibicus')
        num_petals  the number of petal of the flower (eg. '10')
        price       the price of the flower (eg. 15 or 15.0)
        """
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._num_petals

    def get_price(self):
        return self._price


if __name__ == "__main__":
    flowers = []
    flowers.append(Flower("Hibicus", 10, 250.15))
    flowers.append(Flower("Bush Milk", 55, 300))
    flowers.append(Flower("Tiger Nuts", 2000, 5000))

    for c in range(3):
        print(f"Name = {flowers[c].get_name()}")
        print(f"Petals = {flowers[c].get_petals()}")
        print(f"Price = {flowers[c].get_price()}")
        print()
