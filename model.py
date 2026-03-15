# main file
import torch 
import torch.nn as nn


class InputEmbeddings(nn.Modul):
    def __init__(self, d_models: int, vocab_size: int):
        super().__init__()
        