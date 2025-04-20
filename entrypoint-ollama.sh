#!/bin/bash

echo "Ollama server's launching"
ollama serve &
OLLAMA_PID=$!

# Attente du démarrage du serveur
until curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting Ollama's ready on http://localhost:11434 ..."
  sleep 2
done

echo "Model Downloading : ${OLLAMA_MODEL}"
ollama pull "${OLLAMA_MODEL}"

# Garder le serveur en avant-plan
wait $OLLAMA_PID
