#! /bin/bash
source ./pyg/bin/activate
# virtualenv is now active.
#
gcloud auth login
python firebaseListener.py