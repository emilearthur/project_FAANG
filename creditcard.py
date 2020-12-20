class CreditCard:
    """  A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        The initial balance is zerio.

        customer the name """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Returns name of the customer."""
        return self._customer

    def get_bank(self):
        """Returns bank's name."""
        return self._bank

    def get_account(self):
        """Returns the card identifying number."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """ Return current balance."""
        return self._balance

    def charge(self, price):
        """ Charge given price on the card, assuming sufficient
        credit limit.

        Return True if charge was processed; False if charge
        was denied.
        """
        if price + self._balance > self._limit:  # if charge wld exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount

# Testing the class


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("Naa Mensah", "Accra saving",
                             "539 885 223", 2500))
    wallet.append(CreditCard("Naa Mensah", "Accra current",
                             "333 125 233", 3500))
    wallet.append(CreditCard("Naa Mensah", "Accra saving",
                             "333 125 233", 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print(f"Customer = {wallet[c].get_customer()}")
        print(f"Bank = {wallet[c].get_bank()}")
        print(f"Account = {wallet[c].get_account()}")
        print(f"Limit = {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")
        print()
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f"New balance = {wallet[c].get_balance()}")
        print()
