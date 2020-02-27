# encoding: utf-8

from __future__ import absolute_import
from __future__ import print_function
PROTO_COMPILING_ERROR_MSG = ('-------------------------------------------------------------\n'
                             'Error compiling protos. Make sure xproto submodule is updated\n'
                             'Try run: git submodule update --init --recursive\n'
                             '-------------------------------------------------------------')

import functools
import operator
import subprocess
from pathlib2 import Path


PROTO_ROOT_PATHS = ["libs/xproto/loggi"]
PROTO_OUT = "gen_proto"
PROTO_DEPENDENCIES_ROOT_PATHS = ["libs/xproto/third_party"]

# The generated code of these dependencies imports
# modules with the same name of installed packages. (Eg: google)
# To avoid import conflicts, they are excluded from the build and add on requirements/base.txt
PROTO_DEPENDENCIES_BUILD_EXCLUSION = ["libs/xproto/third_party/googleapis-common-protos"]


def list_proto_files(root_paths):
    """Return Protobuf file paths in a given directory."""

    paths = (p for path in root_paths for p in Path(path).glob('**/*.proto'))
    return [p for p in paths if not p.as_posix().startswith(
        tuple(PROTO_DEPENDENCIES_BUILD_EXCLUSION)
    )]


def list_child_dirs(root_paths):
    return [p for path in root_paths if Path(path).is_dir()
            for p in Path(path).iterdir() if p.is_dir()]


def build_protobuf():
    """Build protocol buffers on a given path to Python code."""

    proto_files = list(list_proto_files(PROTO_ROOT_PATHS)) +\
        list(list_proto_files(PROTO_DEPENDENCIES_ROOT_PATHS))

    # If there are not files, just exit, protoc will fail if called without files.
    if not proto_files:
        return

    # Run proto compiler.
    protoc_call = ('python -m grpc_tools.protoc {links} '
                   '--python_out={out} --grpc_python_out={out} {files}').format(
        out=PROTO_OUT,
        links=' '.join('-I {}'.format(path) for path in PROTO_ROOT_PATHS +
                       list_child_dirs(PROTO_DEPENDENCIES_ROOT_PATHS)),
        files=' '.join(file.as_posix() for file in proto_files),
    )

    try:
        subprocess.check_output(protoc_call, shell=True)
    except subprocess.CalledProcessError as e:
        print(PROTO_COMPILING_ERROR_MSG)
        raise e

    def flatten(iterator):
        return functools.reduce(operator.concat, iterator, [])

    def list_subdirectories(path):
        return [path] + flatten([list_subdirectories(p) for p in path.iterdir() if p.is_dir()])

    # Extract all the subdirectories from the root proto out.
    modules = list_subdirectories(Path(PROTO_OUT))

    # Create modules (__init__.py files) so the path can be imported.
    for module in modules:
        module.joinpath("__init__.py").touch()

if __name__ == '__main__':
    build_protobuf()
