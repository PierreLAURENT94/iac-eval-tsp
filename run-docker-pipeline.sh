#!/bin/bash
echo "Entrez vos identifiants AWS :"
read -p "AWS_ACCESS_KEY_ID: " AWS_ACCESS_KEY_ID
read -s -p "AWS_SECRET_ACCESS_KEY: " AWS_SECRET_ACCESS_KEY
echo ""
echo "Enter the Ollama model name, always start with 'Ollama-' (e.g., 'Ollama-codegemma:7b', 'Ollama-llama2:7b', etc.):"
read -p "MODEL_NAME: " MODEL_NAME
echo "$MODEL_NAME choosen"
echo ""
echo "Choose a evaluation strategy :"
echo "1) normal"
echo "2) multi-turn"
echo "3) COT"
echo "4) FSP"
read -p "Choix (1-4): " STRATEGY

STRATEGY_NAME=$(case $STRATEGY in
  1) echo "normal" ;;
  2) echo "multi-turn" ;;
  3) echo "COT" ;;
  4) echo "FSP" ;;
  *) echo "normal" ;;
esac)

echo "Strategy choosen : $STRATEGY_NAME"

echo "RAG is not supported yet with Ollama's LLMs"

echo ""
echo "Enter the number of samples to evaluate (default is 1):"
read -p "SAMPLES: " SAMPLES

if [ -z "$SAMPLES" ]; then
  SAMPLES=1
fi
echo "Number of samples choosen : $SAMPLES"
echo ""

echo "Creating .env file with the following content:"

cat <<EOF > .env
AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
AWS_ROLE_NAME="default"
STRATEGY=$STRATEGY_NAME
MODEL_NAME=$MODEL_NAME
SAMPLES=$SAMPLES
EOF

docker compose up --build -d