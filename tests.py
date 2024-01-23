#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:45:28 2024

@author: christoph
"""

import unittest
import MyEncoder


class Test_encoder(unittest.TestCase):
    
    def test_encoding(self):
        
        # Is encoded text different?
        
        testinput = 'Holla die Waldfee'
        e = MyEncoder.Encoder()
        self.assertNotEqual(e.encode(testinput), testinput, 
                            "Encoder hasn't changed input")
        
        
    def test_randomness(self):
        
        # Test if Encoder encodes randomly for two initialisations
        
        testinput = 'Holla die Waldfee'
        e1 = MyEncoder.Encoder()
        e2 = MyEncoder.Encoder()
        enc_e1 = e1.encode(testinput)
        enc_e2 = e2.encode(testinput)
        self.assertNotEqual(enc_e1, enc_e2, "Encoding not fully random")
        

    def test_encoding_decoding(self):
        
        # Is the text the same after en and decoding?
        
        testinput = 'Holla die Waldfee'
        e = MyEncoder.Encoder()
        enc = e.encode(testinput)
        dec = e.decode(enc)
        self.assertEqual(dec, testinput, "Decoded text not same as input")
        
        
    def test_setting_custom_passphrase(self):
        
        # Test if custom passphrase setting works
        
        testinput = 'Holla die Waldfee'
        
        for pw in [123, 'Password', 12.4]:
        
            with self.subTest(pw):
                
                e1 = MyEncoder.Encoder(pw)
                enc_e1 = e1.encode(testinput)
                
                e2 = MyEncoder.Encoder(pw)
                dec_e2 = e2.decode(enc_e1)

                self.assertEqual(dec_e2, testinput, "Custom seed not working")
        

unittest.main()
