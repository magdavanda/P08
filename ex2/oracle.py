import os
from dotenv import load_dotenv

ENV_VARIABLES: dict[str, str] = {
                            "MATRIX_MODE": "development",
                            "DATABASE_URL": "Connected to local instance",
                            "API_KEY": "Not authenticated",
                            "LOG_LEVEL": "DEBUG",
                            "ZION_ENDPOINT": "Online"
                            }


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    mode = os.getenv("MATRIX_MODE", "development")

    print("Configuration loaded:")

    for var, default in ENV_VARIABLES.items():
        value = os.getenv(var)
        if value is None and var != "API_KEY":
            value = default
            print(f"Using default value for {var}!")
        if var == "MATRIX_MODE":
            var = "Mode"
        elif var == "DATABASE_URL":
            var = "Database"
            if mode == "production":
                value = "Connected to production instance"
            else:
                value = "Connected to local instance"
        elif var == "API_KEY":
            var = "API Access"
            if value is None:
                value = default
            else:
                value = "Authenticated"
        elif var == "LOG_LEVEL":
            var = "Log Level"
        elif var == "ZION_ENDPOINT":
            var = "Zion Network"
        print(f"{var}: {value}")

    print("\nEnvironment security check:")


if __name__ == "__main__":
    main()
