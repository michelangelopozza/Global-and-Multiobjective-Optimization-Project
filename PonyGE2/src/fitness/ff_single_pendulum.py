import numpy as np
from scipy.integrate import odeint
import pandas as pd

np.seterr(divide='raise', over='raise', invalid='raise', under='ignore')

from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff


class ff_single_pendulum(base_ff):
    
    maximise = False

    def __init__(self):
        super().__init__()
    
        self.train_data = self._load_data(params['DATASET_TRAIN'])
        
        # take only x[0] and x[1], not t
        self.y0 = self.train_data[0,1:3]
        
        self.t_eval = self.train_data[:,0]
        self.t_span = [self.train_data[0,0], self.train_data[-1,0]]

        self.y_hat = self.train_data[:,1:3]
        

    def _load_data(self, filepath):
        
        df = pd.read_csv(filepath)
        data_array = df.values
        
        return data_array

    def evaluate(self, ind, **kwargs):

        phenotype_str = ind.phenotype.strip()
        
        # Split the equations
        equations = phenotype_str.split(';')
        
        # if something wrong return some big fitness value
        if len(equations) != 2:
            return 1e10
        
        def system(x, t):
            
            # x[0] = theta
            # x[1] = theta_dot
            try:
                # eval the equations because they are string
                theta_dot = eval(equations[0])
                theta_ddot = eval(equations[1])
            except:
                return [0, 0]
            
            theta_dot = np.clip(theta_dot, -1e5, 1e5)
            theta_ddot = np.clip(theta_ddot, -1e5, 1e5)
            
            return [theta_dot, theta_ddot]
        
        try:

            # eq1 --> x_dot[0] = x[0]
            # eq2 --> x_dot[1] = -b/(L*m**2)*x[1] -g/L*np.sin(x[0])
            sol = odeint(system, self.y0, self.t_eval, full_output=0)
            
            self.y = sol
            
            error_theta = np.mean((self.y[:,0] - self.y_hat[:,0])**2)
            error_theta_dot = np.mean((self.y[:,1] - self.y_hat[:,1])**2)
            
            if np.isnan(error_theta) or np.isnan(error_theta_dot) or np.isinf(error_theta) or np.isinf(error_theta_dot):
                return 1e10
            
            # to reduce long equations with good fitness and ensure exploration
            alpha = 0.001
            complexity_penalty = alpha*len(phenotype_str)
            
            fitness = error_theta + error_theta_dot + complexity_penalty
            
        except Exception as e:
            fitness = 1e10
            

        return fitness
            