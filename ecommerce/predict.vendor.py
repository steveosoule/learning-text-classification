import fasttext

model = fasttext.train_supervised(input="feed.vendor.train.txt", lr=0.5, epoch=25, wordNgrams=2, bucket=200000, dim=50, loss='ova')
model.save_model("model.vendor.bin")

# model = fasttext.load_model("model.vendor.bin")

print(model.test("feed.vendor.valid.txt", k=-1))

input_string = 'lenox  eternal  open  vegetable,  large		DLXET0023'
result = model.predict(input_string, k=-1, threshold=0.3)
print(result)

"""
$ python predict.vendor.py
Read 0M words
Number of words:  48543
Number of labels: 364
Progress: 100.0% words/sec/thread:  175155 lr:  0.000000 loss:  0.897741 ETA:   0h 0m
(16915, 0.0027472527472527475, 1.0)
(('__label__lagos',), array([1.00001001]))
"""