from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / 'data/.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")