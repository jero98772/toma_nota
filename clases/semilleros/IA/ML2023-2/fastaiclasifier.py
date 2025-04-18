from fastai.vision.all import *
import matplotlib.pyplot as plt
path = untar_data(URLs.PETS)
path.ls()
files = get_image_files(path/"images")
len(files)
def label_func(f): return f[0].isupper()
dls = ImageDataLoaders.from_name_func(path, files, label_func, item_tfms=Resize(224))
dls.show_batch()
learn = vision_learner(dls,resnet34,metrics=error_rate)
learn.fine_tune(1)
learn.show_results()
files[0].name
pat = r'^(.*)_\d+.jpg'
plt.show()
#https://docs.fast.ai/tutorial.vision.html
