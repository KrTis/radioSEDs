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
Created on:        Tue Mar 14 11:04:21 2017
Completed on:      
Description:       Plot labels and constants
Result:            None
Requirements:      NumPy
────────────────────────────────────────────────────────────────────────────────
"""
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Packages
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import numpy as np

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Plot Labels
# ──────────────────────────────────────────────────────────────────────────────
# Label         Definition                                 Description
# ──────────────────────────────────────────────────────────────────────────────
SpSt_label      = '$S_P/S_T$'                              # Flux ratio label
SP_label        = '$S_P$ $[\mathrm{\mu Jy}]$'              # Peak flux label
ST_label        = '$S_T$ $[\mathrm{\mu Jy}]$'              # Total flux label
SNR_label       = '$SNR$'                                  # Signal/Noise label
lgSNR_label     = '$\mathrm{lg}\,SNR$'                     # log SNR label
dist_label      = '$d\,\mathrm{[deg]}$'                    # distance in deg
asec_symbol     = " '' "                                   # arcsecond symbol
asec_label      = '$\mathrm{['+asec_symbol+']}$'           # arcsecond in []
deg_label       = '$\mathrm{[deg]}$'                       # degrees in []
ΔRA_label       = 'Right ascension offset '+ asec_label    # α offset label ['']
ΔDEC_label      = 'Declination offset '+ asec_label        # δ offset label ['']
Msol_symbol     = '\mathrm{M_{\odot}}'                     # Solar mass symbol
yr1_symbol      = '\mathrm{yr^{-1}}'                       # Inverse year symbol
Mstar_label     = r'$ M_{\ast}\,['+Msol_symbol+']$'        # Stellar mass symbol
SFR_label       = r'$SFR\,['+Msol_symbol+yr1_symbol+']$'   # SFR label [M0/yr]
lgSratio_label  = r'Normalized log-flux'      # Normalized flux
GHz_label       = r'$[\mathrm{GHz}]$'                      # [GHz] label
lgνrest_label   = r'$\nu_{\mathrm{rest}}$'+GHz_label       # Restframe ν
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Constants
# ──────────────────────────────────────────────────────────────────────────────
# Label         Definition                                 Description
# ──────────────────────────────────────────────────────────────────────────────
μJy             = 10**(-6)                                 # Microjansky
mJy             = 10**(-3)                                 # Milijansky
arcsec          = 1/3600.                                  # Arcsec in degrees
π               = np.pi                                    # Pi number
degtorad        = π/180.                                   # Degrees to radians
σ_interval      = [50, 15.87, 84.13]                       # Median & 1σ
σ_quantile      = [0.16,  0.5 ,  0.84]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# END
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━