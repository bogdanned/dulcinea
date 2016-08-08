from django.dispatch import Signal

#  Sent when the product query is iniated
product_query_initiated = Signal()

# Sent when the product query is finished succesfully
product_query_finished = Signal()

# Sent when the product query has failed
product_query_failed = Signal()
