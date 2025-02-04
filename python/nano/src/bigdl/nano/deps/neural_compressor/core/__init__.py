#
# Copyright 2016 The BigDL Authors.
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
#
from bigdl.nano.utils.log4Error import invalidInputError
try:
    import neural_compressor
except ImportError:
    invalidInputError(
        False,
        errMsg="Intel Neural Compressor must be installed to use quantization.",
        fixMsg="Please install INC by: pip install neural-compressor."
    )

version = neural_compressor.__version__
from .quantization import BaseQuantization
from .base_metric import BaseINCMetric
