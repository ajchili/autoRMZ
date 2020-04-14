# Second round of training

## What was used?
For the second round of training, I used 225 samples that contained 1651 meteors.
This was then fed into a Keras implementation of frcnn that was run for 1 epoch
with a image scale size to 200px for the maximum size on the smallest edge
and was created by
[MasoudKaviani](https://github.com/MasoudKaviani/keras-frcnn). I also added
horizontally and vertically flipped annotated rois.

## How long did it take?
It took roughly an hour.

## What are the results?
Nothing was found!

## Why were these the results?
The image scale size was too small and there was not enough training. This run
was done to see if any results can be found.

## What can be improved?
- Set scale size to be full size of images
- Run for a minimum of 5 epochs
