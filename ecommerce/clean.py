import re
import math
import csv
import pandas as pd
from slugify import slugify

file_name_base = 'feed'

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
	clean_name = name.lower().strip()
	clean_name = clean_name.replace("borsheim's", 'borsheims')
	clean_name = clean_name.replace('\r\n', ' ')
	clean_name = clean_name.replace('&nbsp;', ' ')
	clean_name = clean_name.replace("'' ", '"')
	clean_name = remove_tags(clean_name)
	return clean_name

def create_label(category): 
	return '__label__' + slugify(category)

def clean_and_create_label(category):
	return create_label(clean_string(category))

def parse_categories(categories):
	categories = clean_string(categories).split(',')
	return " ".join(map(create_label, categories))


feed = pd.read_csv(
		file_name_base +'.csv',
		# index_col='Sku',
		encoding='iso-8859-1',
		usecols=usecols,
		converters={
			'Name': clean_string,
			'Category': parse_categories,
			'Description': clean_string,
			'jewelry_catalog_item_no': clean_and_create_label,
			'brand': clean_and_create_label,
			'vendor': clean_and_create_label
		}
	)

feed_count = len(feed.index)
feed_train_count = math.ceil(feed_count * 0.80)
feed_valid_count = math.floor(feed_count * 0.20)

# print(feed.describe`())
# print(feed.head(5))

feed[['Category', 'Name', 'Description', 'Sku']].head(feed_train_count).to_csv(file_name_base +'.category.train.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)
feed[['Category', 'Name', 'Description', 'Sku']].tail(feed_train_count).to_csv(file_name_base +'.category.valid.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)

feed[['brand', 'Name', 'Description', 'Sku']].head(feed_train_count).to_csv(file_name_base +'.brand.train.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)
feed[['brand', 'Name', 'Description', 'Sku']].tail(feed_train_count).to_csv(file_name_base +'.brand.valid.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)

feed[['vendor', 'Name', 'Description', 'Sku']].head(feed_train_count).to_csv(file_name_base +'.vendor.train.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)
feed[['vendor', 'Name', 'Description', 'Sku']].tail(feed_train_count).to_csv(file_name_base +'.vendor.valid.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)

feed[['jewelry_catalog_item_no', 'Name', 'Description', 'Sku']].head(feed_train_count).to_csv(file_name_base +'.jewelry_catalog_item_no.train.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)
feed[['jewelry_catalog_item_no', 'Name', 'Description', 'Sku']].tail(feed_train_count).to_csv(file_name_base +'.jewelry_catalog_item_no.valid.txt', sep="\t", index=False, quoting=csv.QUOTE_NONE, doublequote=False, escapechar=" ", header=False)