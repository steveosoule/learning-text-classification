import fasttext

model = fasttext.train_supervised(input="feed.brand.train.txt", lr=0.5, epoch=25, wordNgrams=2, bucket=200000, dim=50, loss='ova')
model.save_model("model.brand.bin")

# model = fasttext.load_model("model.brand.bin")

print(model.test("feed.brand.valid.txt", k=-1))

input_string = 'lagos  sterling  silver  &  yellow  gold  accent  black  caviar  necklace,  16"	a  black  ceramic  caviar  beaded  16  inch  necklace  that  is  finished  with  signature  lobster  clasp.  ideal  to  pair  with  other  designs  in  the  black  caviar  collection.                  sterling  silver  &amp;  18k  gold          signature  lobster  clasp          width  5mm          length  16  inches  	4OTHN0342'
result = model.predict(input_string, k=-1, threshold=0.3)
print(result)

"""
$ python predict.brand.py
Read 0M words
Number of words:  48543
Number of labels: 237
Progress: 100.0% words/sec/thread:  283868 lr:  0.000000 loss:  0.544569 ETA:   0h 0m
(16976, 0.004219409282700422, 1.0)
(('__label__lagos',), array([1.00001001]))
"""