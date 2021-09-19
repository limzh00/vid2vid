#!/bin/bash
cd ./networks/correlation_package
python3.6 setup.py install --user
cd ../resample2d_package 
python3.6 setup.py install --user
cd ../channelnorm_package 
python3.6 setup.py install --user
cd ..
