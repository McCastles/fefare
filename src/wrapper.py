import argparse
import sys
from .GUI import launch_GUI
from .face_recognition import recognize


def wrap(argv=None):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument('--gui', '-g', help='launch the Graphical User Interface', action='store_true')
    group.add_argument('--version', '-ver', '-v', help='the version of the software', action='store_true')
    group.add_argument('--part', '-p', help='the share of the Eigenfaces to be used', type=float, default=1.0)

    args = parser.parse_known_args()
    req_args = args[1]
    opt_args = args[0]

    if (opt_args.part < 0.0) or (opt_args.part > 1.0):
        sys.exit('Error: this argument must be within the range of 0.0 and 1.0')

    if opt_args.version:
        sys.exit('FeFaRe 1.0.0 (R) McCastles')

    if opt_args.gui:
        launch_GUI()
    else:
        parser.add_argument('train_path', help='the path to the training set')
        parser.add_argument('test_path', help='the path to the test set')
        args = parser.parse_args(req_args)

        verdict = recognize(args.train_path, args.test_path, opt_args.part).get('verdict')
        print(verdict)


if __name__ == "__main__":
    wrap()
