from utils import load_model, get_emb_params
from pathlib import Path
import argparse


def main(args):
    model_path = Path(args.model_path)

    model = load_model(model_path)

    print("Model:", model)

    params = get_emb_params(model)

    print(f"Token size: {params.shape[0]} tokens")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "model_path",
        type=str,
        help="model path",
    )
    args = parser.parse_args()

    main(args)
