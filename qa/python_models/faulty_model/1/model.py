# Copyright 2024, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json
import time

import numpy as np
import triton_python_backend_utils as pb_utils


class TritonPythonModel:
    @staticmethod
    def auto_complete_config(auto_complete_model_config):
        # TYPO to cause error in load
        input0 = {"nameas": "INPUT0", "data_type": "TYPE_FP32", "dims": [4]}
        auto_complete_model_config.add_input(input0)

    def initialize(self, args):
        self.model_config = json.loads(args["model_config"])

    def execute(self, requests):
        """This function is called on inference request."""
        # Less than collector timeout which is 10
        time.sleep(2)
        responses = []
        for _ in requests:
            # Include one of each specially parsed JSON value: nan, inf, and -inf
            out_0 = np.array([1], dtype=np.float32)
            out_tensor_0 = pb_utils.Tensor("OUTPUT0", out_0)
            responses.append(pb_utils.InferenceResponse([out_tensor_0]))

        return responses