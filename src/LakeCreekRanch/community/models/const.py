
class SaleStatus(object):
    """Status of For Sale Objects"""
    FOR_SALE = 1
    SOLD = 2
    SALE_PENDING = 3

    CHOICES = (
        (FOR_SALE, 'For Sale'),
        (SOLD, 'Sold'),
        (SALE_PENDING, 'Sale Pending')
    )