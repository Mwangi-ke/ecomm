
def calculate_discounted_price(price,percentage_discount):
    discount_amount=price*(percentage_discount/100)
    discounted_price=price-discount_amount
    return discounted_price