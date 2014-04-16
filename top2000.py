import os

from awis import AwisApi

ACCESS_ID = os.environ.get('AWS_ACCESS_ID', None)
SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
assert (ACCESS_ID and SECRET_ACCESS_KEY), "You must set credentials in the environment."

api = AwisApi(ACCESS_ID, SECRET_ACCESS_KEY)
#tree = api.top_info(count=10, offset=0, path='Top', recursive=True, descriptions=True)
tree = api.url_info("www.dailydot.com", "Rank", "LinksInCount")
