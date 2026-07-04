from app.core.engine import Engine

def main():
    engine = Engine()

    print("=" * 40)
    print("Khala Nosa Engine Test")
    print("=" * 40)

    messages = [
        "السلام عليكم",
        "",
        "عاملة إيه يا خالة نوسة؟"
    ]

    for msg in messages:
        print(f"\nUser : {msg!r}")
        print(f"Nosa : {engine.process(msg)}")

if __name__ == "__main__":
    main()
