import numpy as np
from scipy.integrate import odeint
import pandas as pd

np.seterr(divide='raise', over='raise', invalid='raise', under='ignore')

from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff


class ff_double_pendulum(base_ff):
    
    maximise = False

    def __init__(self):
        super().__init__()
        
        self.train_data = self._load_data(params['DATASET_TRAIN'])
        
        # take only x[0], x[1], x[2], x[3], not t
        self.y0 = self.train_data[0,1:5]
        
        self.t_eval = self.train_data[:,0]
        self.t_span = [self.train_data[0,0], self.train_data[-1,0]]

        self.y_hat = self.train_data[:,1:5]
        

    def _load_data(self, filepath):
        
        df = pd.read_csv(filepath)
        data_array = df.values
        
        return data_array

    def evaluate(self, ind, **kwargs):

        phenotype_str = ind.phenotype.strip()
        
        # Split the equations
        equations = phenotype_str.split(';')
        
        # if something wrong return some big fitness value
        if len(equations) != 4:
            return 1e10
        
        
        def system(x, t):
            
            # x[0] = theta1
            # x[1] = theta1_dot
            # x[2] = theta2
            # x[3] = theta2_dot
            try:
                # eval the equations because they are string
                theta1_dot = eval(equations[0])
                theta1_ddot = eval(equations[1])
                theta2_dot = eval(equations[2])
                theta2_ddot = eval(equations[3])    
            except:
                return [0, 0, 0, 0]
            
            theta1_dot = np.clip(theta1_dot, -1e5, 1e5)
            theta1_ddot = np.clip(theta1_ddot, -1e5, 1e5)
            theta2_dot = np.clip(theta2_dot, -1e5, 1e5)
            theta2_ddot = np.clip(theta2_ddot, -1e5, 1e5)
            
            return [theta1_dot, theta1_ddot, theta2_dot, theta2_ddot]
        
        try:
            
            # compute x_dot
            sol = odeint(system, self.y0, self.t_eval, full_output=0)
            
            self.y = sol
            
            error_theta1 = np.mean((self.y[:,0] - self.y_hat[:,0])**2)
            error_theta1_dot = np.mean((self.y[:,1] - self.y_hat[:,1])**2)
            error_theta2 = np.mean((self.y[:,2] - self.y_hat[:,2])**2)
            error_theta2_dot = np.mean((self.y[:,3] - self.y_hat[:,3])**2)
            
            if np.isnan(error_theta1) or np.isnan(error_theta1_dot) or np.isinf(error_theta1) or np.isinf(error_theta1_dot):
                    print("AA")
                    return 1e10
            
            if np.isnan(error_theta2) or np.isnan(error_theta2_dot) or np.isinf(error_theta2) or np.isinf(error_theta2_dot):
                    print("BB")
                    return 1e10
            
            # to reduce long equations with good fitness and ensure exploration
            alpha = 0.001
            complexity_penalty = alpha*len(phenotype_str)
            
            fitness = error_theta1 + error_theta1_dot + error_theta2 + error_theta2_dot + complexity_penalty
        except Exception as e:
            print("CC")
            fitness = 1e10

        return fitness
            