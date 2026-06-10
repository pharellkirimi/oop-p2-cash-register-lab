class CashRegister:
    def __init__(self, discount=0):
        # Ensure discount is valid
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    # Getter/Setter style validation for discount
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # update total
        self.total += price * quantity

        # store item names (repeat per quantity if needed)
        for _ in range(quantity):
            self.items.append(item)

        # store transaction history
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        # Remove last transaction
        last = self.previous_transactions.pop()

        # Undo its effect on items and total
        self.total += last["price"] * last["quantity"]

        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])

        print(f"After the discount, the total is ${self.total:.2f}")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()

        # Remove cost
        self.total -= last["price"] * last["quantity"]

        # Remove items
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])