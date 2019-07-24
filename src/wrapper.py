import argparse
import sys
import os
from .GUI import launch_GUI
from .face_recognition import recognize


def wrap(argv=None):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--version', '-ver', '-v', help='the version of the software', action='version', version='FeFaRe 1.0.0')
    parser.add_argument('--part', '-p', help='the share of the Eigenfaces to be used, float 0.0 - 1.0', type=float, default=1.0)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', help='run via text-based CLI, requires paths to training and testing sets', nargs=2, metavar=('TRAIN', 'TEST'))
    group.add_argument('--gui', '--GUI', '-g', help='run via GUI', action="store_true")

    args = parser.parse_args()

    if (args.part < 0.0) or (args.part > 1.0):
        sys.exit('Error: this argument must be within the range of 0.0 and 1.0')

    if args.gui:
        launch_GUI()
    elif args.c:
        verdict = recognize(args.c[0], args.c[1], args.part).get('verdict')
        print('Result:', verdict)
    else:
        print('Run python fefare -h for usage information.')

if __name__ == "__main__":
    wrap()
