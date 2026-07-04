from pathlib import Path

PROJECT_STRUCTURE = [
    "app/api",
    "app/core",
    "app/ai/providers",
    "app/memory",
    "app/personalities",
    "app/skills",
    "app/services",
    "app/database",
    "app/models",
    "app/schemas",
    "app/utils",
    "data/recipes",
    "data/prompts",
    "data/tips",
    "docs",
    "tests",
    "logs",
    "static",
    "templates",
]

INIT_FILES = [
    "app/__init__.py",
    "app/api/__init__.py",
    "app/core/__init__.py",
    "app/ai/__init__.py",
    "app/ai/providers/__init__.py",
    "app/memory/__init__.py",
    "app/personalities/__init__.py",
    "app/skills/__init__.py",
    "app/services/__init__.py",
    "app/database/__init__.py",
    "app/models/__init__.py",
    "app/schemas/__init__.py",
    "app/utils/__init__.py",
]

def create_structure():
    for folder in PROJECT_STRUCTURE:
        Path(folder).mkdir(parents=True, exist_ok=True)

    for file in INIT_FILES:
        Path(file).touch(exist_ok=True)

    print("✅ Khala Nosa project structure verified.")

if __name__ == "__main__":
    create_structure()
