#!/bin/bash
# Run all Botswana MVPs simultaneously

cd thutofund && python app.py &
echo "Started ThutoFund on port 9000"

cd ../lekgetho && python app.py &
echo "Started Lekgetho on port 9001"

cd ../ditshetelo && python app.py &
echo "Started Ditshetelo on port 9002"

cd ../dikgwebo && python app.py &
echo "Started Dikgwebo on port 9003"

echo "All MVPs running. Press Ctrl+C to stop."
wait
