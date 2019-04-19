#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy              as np
import matplotlib.pyplot  as plt
from   matplotlib.patches import Ellipse
import corner
import emcee


class mcmc:
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
Created on:        Mon Nov  6 13:00:52 2017 
Description:       MCMC class with corner plots 
Requirements:      Numpy, matplotlib, corner, emcee
────────────────────────────────────────────────────────────────────────────────
    """
    def __init__(self, 
                 data    : 'x, y, yerr', 
                 fit     : 'fitting function', 
                 lims    : 'parameter interval [min, max]', 
                 priorF  : 'prior PDF'                    = None,  
                 walkers : 'number of walkers'            = 100, 
                 ndim    : 'number of fitting parameters' = 2):
        '''
        A function that produces MCMC error estimation w/ x, y, and σ data.
        Parameters space is limited by lims, [R^n, R^n].
        Prior function is a uniform prior by default
        Number of walkers and number of parameters are chosen here. 
        '''
        self.x, self.y, self.err = data
        self.fit                 = fit
        self.lims                = lims
        self.ndim                = ndim
        self.walkers             = walkers

        if priorF is None:
            self.priorF = self._uniform_prior
        else:
            self.priorF  = priorF
        

    def _model(
            self,
            θ:'parameters')->'f(x, Θ)->f(x)':
        '''
        A function wrapper.
        '''
        return self.fit(θ, self.x)
    
    def χ2(self, θ):
        '''
        The cost function
        '''
        lnprior = self.priorF(θ)

        if not np.isfinite(lnprior):
            return -np.inf

        return lnprior-0.5*np.sum(
            (self.y-self._model(θ))**2/self.err**2)
    
    def _give_θ(
            self, 
            cov:'Covariance matrix 2x2')->'angle':
        '''
        Gives the angle of the covariance matrix
        '''
        return 0.5*180*np.arctan(2*cov[1, 0]/
                                  (cov[0, 0]-cov[1, 1]))/np.pi

    def make_priors(
            self, 
            fun  : 'function that creates a prior' = np.random.uniform,
            pars : '*args of fun'                  = None):
        '''
        Stores initial values of MCMC to self.priors
        '''
        if pars is None:
            pars = self.lims
        self.priors = np.array([fun(*pars) 
                                for _ in range(self.walkers)])

    def run(
            self, 
            Nsamples : 'Chain length'                           = 1000,
            crop     : 'Remove first N elements from the chain' = 50):
        '''
        Runs MCMC and reshapes the result
        '''
        sampler = emcee.EnsembleSampler(
                    self.walkers,
                    self.ndim, 
                    self.χ2)
        
        sampler.run_mcmc(self.priors, Nsamples)
        self.output =\
            sampler.chain[:, crop:, :].reshape((-1, self.ndim))
            
    def _uniform_prior(
            self,
            θ : 'parameters to be cut')->'0 or inf':
        '''
        Zero if θ within limits, infinity outside.
        '''
        θ_l, θ_u = self.lims
        if np.logical_and.reduce(θ<θ_u) and\
           np.logical_and.reduce(θ>θ_l):
            return 0.
        else:
            return np.inf
        
    def plot(
            self, 
            *args    : 'pass to corner',
            levels   : 'contours (default is sigmas)' = \
                [1-np.exp(-k**2/2.)for k in range(1, 4)],
            μ_1      : 'first moments'                = None, 
            μ_2      : 'covariance matrix'            = None,
            ecolor   : 'ellipse color'                = 'r',
            ealpha   : 'ellipse alpha'                = 1,
            N_CI     : "which confidence intervals to plot" = [1],
            **kwargs : 'pass to corner'):
        ''' 
        Creates a corner plot and draws an ellipse of the covariance matrix
        if the covariance matrix is provided.
        '''
        self.axes = corner.corner(
            self.output, 
            *args,
            truths = μ_1, 
            levels = levels,
            **kwargs)

        if μ_2 is not None:
            for i in range(self.ndim):
                for j in range(i):
                    try:
                        μ      = μ_1[[j, i]]
                        cov    = μ_2[np.ix_([j, i],
                                            [j, i])]
                        λ, v   = np.linalg.eig(cov)
                        w      = np.sqrt(λ)
                        for k in N_CI:
                            self.axes.axes[self.ndim*(i)+j].add_patch(
                                Ellipse(
                                    xy        = μ,
                                    width     = 2*k*w[0],
                                    height    = 2*k*w[1],
                                    angle     = self._give_θ( cov) ,
                                    edgecolor = ecolor,
                                    fill      = False,
                                    lw        = 2,
                                    alpha     = ealpha,
                                        ))
                    except:
                        pass


