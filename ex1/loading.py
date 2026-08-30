def dependencies_check() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    check: bool = True

    try:
        import pandas
        print(f" [OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ModuleNotFoundError:
        print(" [KO] pandas missing")
        check = False

    try:
        import numpy
        print(
                f" [OK] numpy ({numpy.__version__}) "
                f"- Numerical computation ready")
    except ModuleNotFoundError:
        print(" [KO] numpy missing")
        check = False

    try:
        import matplotlib
        print(
                f" [OK] matplotlib ({matplotlib.__version__}) "
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
        scores: numpy.ndarray = numpy.random.randint(0, 100, 1000)
        levels: numpy.ndarray = numpy.random.randint(0, 10, 1000)

        import pandas
        data_frame: pandas.DataFrame = pandas.DataFrame(
            {
                "score": scores,
                "level": levels
            }
        )
        max_score: int = data_frame["score"].max()
        max_level: int = data_frame["level"].max()
        # print(f"Max score: {max_score}")
        # print(data_frame)

        print("Generating visualization...")
        import matplotlib.pyplot
        matplotlib.pyplot.hist(data_frame["score"])
        matplotlib.pyplot.title("Tournament statistics")
        matplotlib.pyplot.xlabel("Score")
        matplotlib.pyplot.ylabel("Players")
        matplotlib.pyplot.figtext(0.01, 0.01, f"Max score: {max_score}")
        matplotlib.pyplot.figtext(0.01, 0.05, f"Max level: {max_level}")
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
