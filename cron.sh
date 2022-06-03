#!/bin/bash


# create a timestamp alias for the commit message
timestamp() {
  date +"%Y-%m-%d @ %T"
}

# Go to the repo 
cd /home/pi/BuildingAnAQSensorNetwork

echo "Job started: $(timestamp)" >> log.txt

# pull & push
if [[ `git status --porcelain` ]]; then
  echo "Running Git commands: $(timestamp)" >> logs/log.txt
  git pull origin main
  git add .
  git commit -m "Update: $(timestamp)"
  git push https://github.com/lalitshankarchowdhury/BuildingAnAQSensorNetwork
  echo "Finished running Git commands: $(timestamp)" >> logs/log.txt
fi

echo "Job done: $(timestamp)" >> log.txt
echo "-------------------------------------------" >> logs/log.txt