import logging
from qobuz_dl.core import QobuzDL
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

# Configuração do logging
logging.basicConfig(level=logging.INFO)

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

qobuz = QobuzDL()
qobuz.get_tokens()
qobuz.initialize_client(email, password, qobuz.app_id, qobuz.secrets)

qobuz.handle_url("https://play.qobuz.com/album/va4j3hdlwaubc")