from distutils.core import setup

setup(
    name='autoRMZ',
    version='0.0.1',
    packages=['tensorflow', 'numpy', 'opencv-python', 'numpy'],
    url='https://github.com/ajchili/autoRMZ',
    license='MIT',
    author='ajchili (Kirin Patel)',
    author_email='kirinpatel@gmail.com',
    description='A TensorFlow application built to help detect meteors within spectrograms, inspired by Radio Meteor '
                'Zoo on zooniverse.org.'
)
