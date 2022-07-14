#Google Fact check script - that pulls information already classified in Google

#!/bin/bash

echo "Enter the fact to be checked:"

read test_string

echo "Checking $test_string"

curl \
  'https://factchecktools.googleapis.com/v1alpha1/claims:search?query=Vaccine20%causes20%autism20%&key=AIzaSyBHU_ic4FPPateUq8f7umlJ3lg1mb7FDFA' \
  --header 'Accept: application/json' \
  --compressed

:'
curl \
  'https://factchecktools.googleapis.com/v1alpha1/claims:search?query=Trump%20rigged%20elections&key=AIzaSyBHU_ic4FPPateUq8f7umlJ3lg1mb7FDFA' \
  --header 'Accept: application/json' \
  --compressed
'

