#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
────────────────────────────────────────────────────────────────────────────────
Author:        Krešimir Tisanić
Email:         kresimir.tisanic@gmail.com
Project:       SFG SED
Created on:    Mon Mar 13 11:27:21 2017
Description:   Definition of the COSMOS field
Result:        A function giving a True/False numpy array for given α and δ
Requirements:  Numpy
────────────────────────────────────────────────────────────────────────────────
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Packages
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import numpy as np

# ──────────────────────────────────────────────────────────────────────────────
#  Definitions
# ──────────────────────────────────────────────────────────────────────────────

COSMOS_α = 150.11916667               # Position of the COSMOS field center
COSMOS_δ = 2.20583333                 # Position of the COSMOS field center
COSMOS_w = np.sqrt(2)/2               # Half-side of the cosmos field

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Main
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def COSMOS_cut(α, δ):
    """
    Description
    ===========
    This function gives a numpy True/False array that is True for objects that
    are within 2 deg2 square area centered around the COSMOS field.
    
    Parameters
    ==========
    α: float array
       Right ascension numpy array
    δ: float array
       Declination numpy array

    Returns
    =======
    array: numpy
           a numpy True/False array of the same format as α and δ
    """
    α_cut = np.logical_and(α > COSMOS_α-COSMOS_w, α < COSMOS_α+COSMOS_w)
    δ_cut = np.logical_and(δ > COSMOS_δ-COSMOS_w, δ < COSMOS_δ+COSMOS_w)
    return np.logical_and(α_cut, δ_cut)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# End
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
