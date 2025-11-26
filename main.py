from utils import greet
from models import Fish
from config import GAME_TITLE

def main():
    print(f"=== {GAME_TITLE} ===")
    greet("Player")

    salmon = Fish("Salmon", 250)
    print(salmon.info())

if __name__ == "__main__":
    main()
