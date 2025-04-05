# ENDPOINTS:
# OPENAI SDK OLLAMA BASE URL
OAPI_OPENAISDK_BASE_URL = 'http://localhost:11434/v1'
OLLAPI_ENDPOINT_BASE = 'http://localhost:11434/v1'
# OLLAMA API ENDPOINTS
OAPI_GENERATE_URL = 'http://localhost:11434/api/generate'
OAPI_CHAT_URL = 'http://localhost:11434/api/chat'
OAPI_EMBED_URL = 'http://localhost:11434/api/embed'

# DEEPSEEK API ENDPOINTS
DEEPSEEK_API_URL = "https://api.deepseek.com"
# --------------------

# MODELS:
# embedding
OMODEL_E5LARGE = "jeffh/intfloat-multilingual-e5-large-instruct:f32"
OMODEL_NOMIC = "nomic-embed-text:latest" # 768 Dimensionen

# generation
OMODEL_LLAMA3D2 = "llama3.2:latest"
OMODEL_MISTRALNEMO = "mistral-nemo:latest"
OMODEL_GEMMA = "gemma3:latest"

# multimodal
OMODEL_LLAVA = "llava:latest"

# reasoning
OMODEL_DEEPSEEK='deepseek-r1:14b' # does not support tools!
# --------------------

# VECTOR STORAGE:
MILVUS_DB = "./milvus_db.db"
MILVUS_COLLECTION_A = "milvus_collection_a"

# KEYS:
# ollama
OLLAMA_FAKE_API_KEY = 'ollama'
DEEPSEEK_API_KEY = ""
# --------------------

# PATHS:
ASSETS_PATH = 'notebooks/assets'
# --------------------