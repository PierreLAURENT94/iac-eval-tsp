#!/bin/bash

set -e

echo "🔧 setup.sh launching..."
bash ./setup.sh

CONFIG_FILE="config_${MODEL_NAME}_${STRATEGY}.json"

# File config json creation
if [ ! -f "$CONFIG_FILE" ]; then
  echo "Creation of $CONFIG_FILE..."
  cat <<EOF > "$CONFIG_FILE"
{
  "samples": ${SAMPLES},
  "models": [
    "${MODEL_NAME}"
  ]
}
EOF
else
  echo "File $CONFIG_FILE already exists, skipping creation."
fi

# Evalution command construction
CMD="python3 evaluation/eval.py"
if [ "$STRATEGY" != "normal" ]; then
  CMD="$CMD --enhance-strat $STRATEGY"
fi
CMD="$CMD --config=$CONFIG_FILE"

echo "Command to be executed: $CMD"
eval $CMD
