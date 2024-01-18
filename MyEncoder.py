#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:43:18 2024

THE ENCODER

Takes an input (string) and encodes the imput. Can also decode.


@author: christoph
"""


import numpy as np
import string
import time


def generate_random_number():
    """
    Creates a random number based on the time of the call.
    Would be fun to make it more sophisticated in the future.

    Returns
    -------
    Random integer number.

    """
    
    # Get current time
    t = time.time()
    # use all digits (i.e., multiply by 1e7 and use as integer)
    rand = int(t*1e7)
    
    return rand



class Encoder:
    """
    
    """
    
    def __init__(self, seed=None):  # SEED AS OPTIONAL INPUT???
    
        if seed is None:
            self.rand_seed = generate_random_number()
        else:
            self.rand_seed = seed

        self.rng = np.random.default_rng(self.rand_seed)
        self.all_chars = string.printable
        self.indices_plain = np.arange(len(self.all_chars)) # 0 to 99
        self.indices_shuffled = self.rng.permuted(self.indices_plain)
        self.indices_unshuffled = np.argsort(self.indices_shuffled)
        
        
    def get_character_index(self, txt):
        character_index = []
        for char in txt:
            character_index.append(self.all_chars.rfind(char))
        return character_index
        
    
    def encode(self, txt):
        txt_indices_plain = self.get_character_index(txt)
        txt_encoded = ''
        for i in txt_indices_plain:
            txt_encoded += self.all_chars[self.indices_shuffled[i]]
        return txt_encoded
    
    
    def decode(self, txt_encoded):
        txt_indices_encoded = self.get_character_index(txt_encoded)
        txt_decoded = ''
        for i in txt_indices_encoded:
            txt_decoded += self.all_chars[self.indices_unshuffled[i]]
        return txt_decoded

