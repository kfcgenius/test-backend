"""Main module with FastAPI routes"""

import random
import string

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/strings/random")
def generate_random_string():
    """Generates random string and returns it as JSON"""

    alphabet = string.ascii_letters + string.digits
    random_chars = random.choices(alphabet, k=10)  # nosec B311
    random_string = "".join(random_chars)

    return {"random_string": random_string}
