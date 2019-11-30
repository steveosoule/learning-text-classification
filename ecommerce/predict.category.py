import fasttext

model = fasttext.train_supervised(input="feed.category.train.txt", lr=0.5, epoch=25, wordNgrams=2, bucket=200000, dim=50, loss='ova')
model.save_model("model.category.bin")

# model = fasttext.load_model("model.category.bin")

print(model.test("feed.category.valid.txt", k=-1))

input_string = "14k  rose  gold  diamond  halo  ring  mounting,  0.09cttw	finish  off  your  vintage-inspired  look  with  the  14k  rose  gold  diamond  halo  ring  mounting.  crafted  in  14k  rose  gold,  this  ring  mounting  is  highlighted  with  prong-set  halo  formed  by  12  round  diamonds  weighing  0.09cttw.  a  center  round  diamond  of  your  choice  (sold  separately)  adds  splendor  to  this  enticing  piece.  additional  sizes  may  be  available  by  special  order.  for  more  information,  please  call  800.642.gift  or  email  us  at  customercare@borsheims.com.	2FSSZ0252"
result = model.predict(input_string, k=-1, threshold=0.3)
print(result)

"""
$ python predict.category.py
Read 0M words
Number of words:  48543
Number of labels: 709
Progress: 100.0% words/sec/thread:  134200 lr:  0.000000 loss:  3.017963 ETA:   0h 0m
(17084, 0.007916661025137882, 0.9933802962809489)
(('__label__engagement-ring-settings', '__label__halo-engagement-ring-settings', '__label__new-engagement-rings-settings'), array([0.99768686, 0.97703266, 0.37755069]))
"""