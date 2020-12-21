class CreditCard:
    """  A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        The initial balance is zero.

        customer    the customer the name (eg. 'Emile Mensah')
        bank        the name of the bank (eg. 'Accra Bank')
        acnt        the account identifier (eg. '532 552 353')
        limit       the credit limit (measured in usd)
        """
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


# class extension (Inheritance)
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """ Create anew predatory credit card instance.
        The initial balance is zero.

        customer    the customer the name (eg. 'Emile Mensah')
        bank        the name of the bank (eg. 'Accra Bank')
        acnt        the account identifier (eg. '532 552 353')
        limit       the credit limit (measured in usd)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and asses $5 if charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self._balance += 5  # asses penalty
        return success          # caller expects return value

    def process_month(self):
        """Asses monthly interest on outstanding balance."""
        if self._balance > 0:
            # if postive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor

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
