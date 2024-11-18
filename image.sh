source .env
curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "dall-e-3",
    "prompt": "MeshCluster a novel distributed system architecture for managing local energy and computing resources, MESH CLUSTER: Adaptive Infrastructure for Critical Situations",
    "n": 1,
    "size": "1024x1024"
  }'

