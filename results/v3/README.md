# Second round of training

## What was used?
- 225 samples consisting of 1651 annotated meteors
- frcnn in Keras
- 5 epochs of training
- Horizontally and vertically flipped annotations
- Full size sample images

Keras implementation by
[MasoudKaviani](https://github.com/MasoudKaviani/keras-frcnn).

## How long did it take?
Over 30 hours.

## What are the results?
Nothing was found!

## Why were these the results?
These were likely the results of a mis-applied model. Upon further reflection of
my data set and the model's intended application, it is likely that the model
used, MasoudKaviani's implementation of an FRCNN is not built to detect the
differences between small specs in a JPEG image. This is likely why, even when
using the full resolution images, no results were found when training version 3
of the model.

## What can be improved?
- Investigate the MNIST model code provided by Keras to develop a more refined
model that focuses on smaller features.
