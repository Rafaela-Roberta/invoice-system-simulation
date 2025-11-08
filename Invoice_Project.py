from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.cost = 0
        self.items = []
        self.comments = [] # list of strings representing comments on the invoice

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)
    
        """ Bug fix explanation:
        The previous code applied the discount incorrectly by mixing the discount with the tax calculation.
        Now, the discount is applied to the item's price first, and then tax is calculated on the discounted price.
        The 'discount' value must be provided as a decimal, for example: 0.20 for 20%.
        """

    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]
            discounted_price = price * (1 - discount)
            final_price = discounted_price + (1 * tax)
            total += final_price
            
        return total
    
    def add_comment(self, comment): # add a comment to the invoice
        self.comments.append(comment)
        
    def get_comments(self): # Return all comments as a single string
        if not self.comments:
            return "No comments available."
        return "\n".join(self.comments)

if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    
    invoice.add_comment("Payment due in 30 days.")
    invoice.add_comment("Please make checks payable to Rafaela Silva.")
    invoice_total = invoice.calculate_total(0.20)  # Instead of 20, I had changed for 0.20 to apply a 20% discount
    print(invoice_total)
    print("\nComments on Invoice:")
    print(invoice.get_comments())
    