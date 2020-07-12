# Copyright 2019 D-Wave Systems Inc.
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

import itertools
import os

import matplotlib
matplotlib.use("agg")    # must select backend before importing pyplot
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import pandas as pd

# D-Wave Ocean tools
import dimod
from dwave.embedding.chimera import find_clique_embedding
from dwave.system import DWaveSampler, EmbeddingComposite


Q = {('x0', 'x0'): 1, ('x0', 'x1'): 4, ('x0', 'x2'): 8, ('x0', 'x3'): 16, ('x0', 'x4'): 32, ('x1', 'x2'): 16, ('x1', 'x3'): 32, 
    ('x1', 'x4'): 64, ('x2', 'x3'): 64, ('x2', 'x4'): 128, ('x3', 'x4'): 256, ('x1', 'x1'): 4, ('x2', 'x2'): 16, ('x3', 'x3'): 64, 
    ('x4', 'x4'): 256}
 
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=1000)
print(sampleset.first.sample)
print(sampleset.first.energy)
