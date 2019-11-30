curl https://www.borsheims.com/godatafeed/godatafeed.csv -o feed.csv
head -n 100 feed.csv > feed.sample.csv
pip install pandas python-slugify