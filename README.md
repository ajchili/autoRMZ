# autoRMZ
A TensorFlow application built to help detect meteors within spectrograms, inspired by Radio Meteor Zoo on zooniverse.org.

### hardcoded.py
A handmade algorithm written in Python 3 used to determine necessary filters for a cnn.

#### How to use
1. Create an account with [brams](http://brams.aeronomie.be/)
2. Check data availability [here](http://brams.aeronomie.be/availability/) after signing in
3. Download data within the determined availability [here](http://brams.aeronomie.be/data/)
4. Place downloaded images within the **dataset/test_set** directory
5. Install dependencies via setup.py
6. run `python hardcoded.py`
