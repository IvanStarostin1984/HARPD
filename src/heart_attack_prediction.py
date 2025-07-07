import argparse
import sys
from pathlib import Path


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
    data_path = Path(args.data)
    if not data_path.is_file():
        print(f"Dataset not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Placeholder - dataset: {data_path}, output directory: {args.out}")


if __name__ == "__main__":
    main()
