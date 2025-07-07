import argparse


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Heart Attack Risk Prediction placeholder"
    )
    parser.add_argument(
        "--data",
        required=True,
        help="Path to dataset CSV",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Directory to store outputs",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Placeholder - dataset: {args.data}, output directory: {args.out}")


if __name__ == "__main__":
    main()
