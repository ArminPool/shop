import datetime
from haystack import indexes
from product.models import Posts


class PostsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
   # product = indexes.CharField(model_attr='product_name')

    def get_model(self):
        return Posts

