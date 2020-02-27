# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import sys

sys.path.insert(0, '/home/ericktakeshi/loggi/grpc-python-client/gen_proto/')

import logging

import grpc

import gen_proto.one.order.v1.pickup_scheduler_api_pb2 as pickup_scheduler_api_pb2
import gen_proto.one.order.v1.pickup_scheduler_api_pb2_grpc as pickup_scheduler_api_pb2_grpc


def greet(stub):
    request = pickup_scheduler_api_pb2.PickupOrderScheduleRequest(id=1)
    response = stub.PickupOrderSchedule(request)
    print(response)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pickup_scheduler_api_pb2_grpc.PickupSchedulerAPIStub(channel)
        greet(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
