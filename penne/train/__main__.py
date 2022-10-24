import argparse
import shutil
from pathlib import Path

import penne


###############################################################################
# Entry point
###############################################################################


def main(config, datasets, gpus=None):
    # Create output directory
    directory = penne.RUNS_DIR / config.stem
    directory.mkdir(parents=True, exist_ok=True)

    # Save configuration
    shutil.copyfile(config, directory / config.name)

    # Train
    penne.train.run(
        datasets,
        directory,
        directory,
        directory,
        gpus)

    # Evaluate
    penne.evaluate.datasets([dataset], directory, gpus)


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument(
        '--config',
        type=Path,
        default=penne.DEFAULT_CONFIGURATION,
        help='The configuration file')
    parser.add_argument(
        '--datasets',
        nargs='+',
        default=['mdb', 'ptdb'],
        help='The datasets to train on')
    parser.add_argument(
        '--gpus',
        type=int,
        nargs='+',
        help='The gpus to run training on')
    return parser.parse_args()


if __name__ == '__main__':
    main(**vars(parse_args()))
