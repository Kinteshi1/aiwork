# === Data Science & Machine Learning ===
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

# === Vector Database ===
from pymilvus import DataType, MilvusClient

# === HTTP & Web ===
import httpx
import requests
from dotenv import load_dotenv
from duckduckgo_search import DDGS

# === Utilities ===
from tqdm import tqdm
import nest_asyncio
from rich import print as rprint

# === Data Models ===
from pydantic import BaseModel, Field