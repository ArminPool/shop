import datetime
from haystack import indexes
from product.models import Post


"""
Thanks to haystack we can search models
"""


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # Text is that u want to search
    # Here text cant be only Return Value from __str__ method under Model
    text = indexes.CharField(document=True, use_template=True)
   # product = indexes.CharField(model_attr='product_name')

    def get_model(self):
        return Post

