#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
────────────────────────────────────────────────────────────────────────────────
Author:            Krešimir Tisanić
Email:             kresimir.tisanic@gmail.com
Project:           SFG SED
Institution:       Department of Physics,
                   Faculty of Science,
                   University of Zagreb,
                   Bijenička cesta 32,
                   10000  Zagreb,
                   Croatia
Created on:        Wed Feb 15 11:37:00 2017
Completed on:
Description:       Error Handling
Result:
Requirements:      
────────────────────────────────────────────────────────────────────────────────
"""

class dimensionError(Exception):
    def __init__(self, θ, dimθ):
        message = "dim(" + θ + ") is not " + str(dimθ)
        super(dimensionError, self).__init__(message)
