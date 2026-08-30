def dependencies_check() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:\n")

    check: bool = True

    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ModuleNotFoundError:
        print(
            "pandas missing\nInstallation"
            " instructions: 'pip install pandas'")
        check = False

    try:
        import numpy
        print(
                f"[OK] numpy ({numpy.__version__}) "
                f"- Numerical computation ready")
    except ModuleNotFoundError:
        print("numpy missing\nInstallation instructions: 'pip install numpy'")
        check = False

    try:
        import matplotlib
        print(
                f"[OK] matplotlib ({matplotlib.__version__}) "
                f"- Visualization ready")
    except ModuleNotFoundError:
        print(
                "matplotlib missing\nInstallation instructions: "
                "'pip install matplotlib'")
        check = False

    return check


def main() -> None:
    if dependencies_check():
        print("Analyzing Matrix Data")
    else:
        return


if __name__ == "__main__":
    main()
