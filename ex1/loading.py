def dependencies_check() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    check: bool = True

    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ModuleNotFoundError:
        print(" [KO] pandas missing")
        check = False

    try:
        import numpy
        print(
                f"[OK] numpy ({numpy.__version__}) "
                f"- Numerical computation ready")
    except ModuleNotFoundError:
        print(" [KO] numpy missing")
        check = False

    try:
        import matplotlib
        print(
                f"[OK] matplotlib ({matplotlib.__version__}) "
                f"- Visualization ready")
    except ModuleNotFoundError:
        print(" [KO] matplotlib missing")

        check = False

    return check


def main() -> None:
    if dependencies_check():
        print("\nAnalyzing Matrix Data...")
        print("Processing 1000 data points...")

        import numpy
        data_to_process: numpy.ndarray = numpy.random.randint(0, 100, (1000, 2))

        import pandas
        data_frame: pandas.DataFrame = pandas.DataFrame(
            data_to_process,
            columns=["score", "level"]
        )
        # max_score: int = data_frame["score"].max()
        # print(f"Max score: {max_score}")
        # print(data_frame)

        print("Generating visualization...")
        import matplotlib.pyplot
        matplotlib.pyplot.hist(data_frame["score"])
        matplotlib.pyplot.title("Tournament statistics")
        matplotlib.pyplot.xlabel("Score")
        matplotlib.pyplot.ylabel("Players")
        file: str = "matrix_analysis.png"
        matplotlib.pyplot.savefig(file)

        print()
        print("Analysis complete!")
        print(f"Results saved to: {file}")

    else:
        print(
                "\n Missing dependencies.\n"
                " Installation with pip:"
                " 'pip install -r requirements.txt'\n"
                " Installation with poetry: 'poetry install'")


if __name__ == "__main__":
    main()
