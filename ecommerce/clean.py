import pandas as pd
import re

input_file = 'feed.csv'
output_file = 'feed.output.csv'

usecols=[
		'Sku',
		'Name',
		'Category',
		'Description',
		'jewelry_catalog_item_no',
		'brand',
		'vendor'
	]

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

def clean_string(name):
	clean_name = name.lower()
	clean_name = clean_name.replace("borsheim's", 'borsheims')
	clean_name = clean_name.replace('\r\n', ' ')
	clean_name = clean_name.replace('&nbsp;', ' ')
	clean_name = remove_tags(clean_name)
	return clean_name

feed = pd.read_csv(
		input_file,
		index_col='Sku',
		encoding='iso-8859-1',
		usecols=usecols,
		converters={
			'Name': clean_string,
			'Category': clean_string,
			'Description': clean_string,
			'jewelry_catalog_item_no': clean_string,
			'brand': clean_string,
			'vendor': clean_string
		}
	)

print(feed.head(5))
# print(feed.describe`())

feed.to_csv(output_file, encoding='utf-8')