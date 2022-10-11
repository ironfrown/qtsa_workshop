# Support functions for QTSA workshop
# Author: Jacob Cybulski, jacob.cybulski[at]deakin.edu.au
# Location: School of IT, SEBE, Deakin University, Melbourne, Vic, Australia
# Aims: Provide support for quantum time series analysis

import matplotlib.pyplot as plt
import numpy as np
import pylab
import math
from typing import Union
from IPython.display import clear_output
from qiskit.utils import algorithm_globals


##### Various small functions

### Own loss function - needs to be instance of Loss
def square_loss(targets, predictions):
    loss = 0
    for t, p in zip(targets, predictions):
        loss += (t - p) ** 2
    loss = loss / len(targets)
    return 0.5*loss


##### Callback functions for regressor

### Callback function that draws a live plot when the .fit() method is called
### - Could change to record weights (TF coefficients?)

# Regressor callback
class Regr_callback:
    name = "Regr_callback"
    
    # Initialises the callback
    def __init__(self, log_interval=50):
        self.objfun_vals = []
        self.log_interval = log_interval

    # Initialise callback lists
    # - For some reason [] defaults not always work (bug?)
    def reset(self, obfun=[]):
        self.objfun_vals = obfun

    # Find the first minimum objective fun value
    def min_obj(self):
        if self.objfun_vals == []:
            return (-1, 0)
        else:
            minval = min(self.objfun_vals)
            minvals = [(i, v) for i, v in enumerate(self.objfun_vals) if v == minval]
            return minvals[0]

    # Creates a simple plot of the objective functionm
    # - Can be used iteratively to make animated plot
    def plot(self):
        clear_output(wait=True)
        plt.rcParams["figure.figsize"] = (12, 6)
        plt.title("Objective function")
        plt.xlabel("Iteration")
        plt.ylabel("Objective function value")
        plt.plot(range(len(self.objfun_vals)), self.objfun_vals, color="blue")
        plt.show()

    # Callback function to store objective function values and plot
    def graph(self, weights, obj_func_eval):
        self.objfun_vals.append(obj_func_eval)
        self.plot()
            
    # Callback function to store objective function values but not plot
    def collect(self, weights, obj_func_eval):
        self.objfun_vals.append(obj_func_eval)
        current_batch_idx = len(self.objfun_vals)
        if current_batch_idx % self.log_interval == 0:
            prev_batch_idx = current_batch_idx-self.log_interval
            last_batch_min = np.min(self.objfun_vals[prev_batch_idx:current_batch_idx])
            print('Regr callback(', prev_batch_idx, ', ', current_batch_idx,') = ', last_batch_min)
            

##### Defines several target functions for testing

### Sample Target functions
### - Each target defines its X range and y range needs to be [0,+1]
### - Assume X is either a scalar, a list or a vector
### - Returns y which is either a scalar, a list or a vector

# Common target class
class Target:
    name = "Target"
    
    # Initialises the target
    def __init__(self):
        self.xmin = -2*np.pi
        self.xmax = +2*np.pi
        self.ymin = 0.0
        self.ymax = 1.0
        self.epsilon = 0.1
        
    # Returns the X range of the function
    def xrange(self):
        return (self.xmin, self.xmax)
    
    # Returns the y range of the function
    def yrange(self):
        return (self.ymin, self.ymax)
    
    # Returns the epsilon (error to be generated)
    def eps(self):
        return self.epsilon
    
    # Returns the main function
    def fun(self, x):
        return x / (2.0*np.pi)
    
    # Plots target data in its natural range
    def plot(self, sample_no=20, color='blue', marker='None', linestyle='solid', ylim='None'):
        sample_x = [self.xmin+i*(self.xmax-self.xmin)/sample_no
                    for i in range(sample_no)]
        sample_y = [self.fun(self.xmin+i*(self.xmax-self.xmin)/sample_no) 
                  for i in range(sample_no)]
        plt.rcParams["figure.figsize"] = (12, 6)
        plt.title('Function "'+self.name+'"')
        plt.xlabel("Range")
        plt.ylabel("Target value")
        if ylim != 'None': plt.ylim(ylim)
        plt.xlim(self.xrange())
        plt.plot(sample_x, sample_y, color=color, marker=marker, linestyle=linestyle)
        plt.show()

# Simple trig function
class Target_sin(Target):
    name = "Target_sin"
    
    def fun(self, x):
        return np.sin(x) / 2.0 + 0.5

# Complex trig function
class Target_2_sins(Target):
    name = "Target_2_sins"
    
    def fun(self, x):
        return (np.sin(5.0 * x) + 0.5*np.sin(8.0 * x)) / 4 + 0.5

# Complex poly function
class Target_poly(Target):
    name = "Target_poly"

    def __init__(self):
        super().__init__()
        self.xmin = -0.9*np.pi
        self.xmax = +1.1*np.pi
        self.epsilon = 0.1
        
    def fun(self, x):
        return -(8*x-4*x**2+0.2*x**3-0.1*x**5)/70+0.1

# Complex poly function
class Target_poly_3(Target):
    name = "Target_poly"

    def __init__(self):
        super().__init__()
        self.xmin = -0.5
        self.xmax = +1
        self.epsilon = 0.1
        
    def fun(self, x):
        return 0.3-0.5*x-x**2+2*x**3

# Complex line function
class Target_line(Target):
    name = "Target_line"

    def __init__(self, slope=0.1, intercept=0.5, xmin=-2.0, xmax=+2.0):
        super().__init__()
        # algorithm_globals.random_seed = np.abs(int(slope+intercept*(xmax-xmin)*100))
        self.xmin = xmin
        self.xmax = xmax
        self.slope = slope
        self.intercept = intercept
        self.epsilon = 0.1
        
    def fun(self, x):
        return self.intercept+self.slope*x

# Complex trig with trend function
class Target_trig_trend(Target):
    name = "Target_trig_trend"

    def __init__(self):
        super().__init__()
        self.xmin = -4.0
        self.xmax = +4.0
        self.epsilon = 0.1
        
    def fun(self, x):
        return 0.5+0.09*x+0.09*np.sin(3*x)+0.15*np.cos(6*x)

# Broken jitter
class Target_jitter(Target):
    name = "Target_jitter"

    def __init__(self):
        super().__init__()
        self.xmin = -6.0
        self.xmax = +6.0
        self.epsilon = 0.1
        self.point_no = 60 # 300
        self.breaks = [-3, 0, 3]
        self.scales = [0.2, 0.8, 0.4, 0.7]
        
    def fun_point(self, x):
        if (x < self.xmin):
            return 0.0
        elif (x < self.breaks[0]):
            return self.scales[0]+self.epsilon*np.random.random()
        elif (x < self.breaks[1]):
            return self.scales[1]+self.epsilon*np.random.random()
        elif (x < self.breaks[2]):
            return self.scales[2]+self.epsilon*np.random.random()
        elif (x < self.xmax):
            return self.scales[3]+self.epsilon*np.random.random()
        else:
            return 0.0
    
    def fun(self, x):
        if type(x) is int or type(x) is float:
            return self.fun_point(x)
        else:
            return np.array([self.fun_point(xi) for xi in x])

# Normalised beer sales data
class Target_beer(Target):
    name = "Target_beer"
    beer_data = [  \
       0.097, 0.0, 0.033, 0.124, 0.113, 0.042, 0.088, 0.08, 0.078, 0.055, \
       0.077, 0.138, 0.148, 0.135, 0.302, 0.165, 0.203, 0.187, 0.203, 0.242, \
       0.353, 0.269, 0.281, 0.357, 0.359, 0.376, 0.631, 0.213, 0.275, 0.281, \
       0.287, 0.291, 0.288, 0.337, 0.426, 0.382, 0.179, 0.165, 0.174, 0.218, \
       0.196, 0.225, 0.22, 0.272, 0.22, 0.273, 0.463, 0.205, 0.274, 0.309, \
       0.541, 0.581, 0.41, 0.095, 0.163, 0.194, 0.325, 0.301, 0.234, 0.147, \
       0.138, 0.132, 0.192, 0.178, 0.295, 0.173, 0.235, 0.299, 0.244, 0.212, \
       0.311, 0.296, 0.531, 0.51, 0.379, 0.447, 0.414, 0.471, 0.776, 0.344, \
       0.389, 0.353, 0.366, 0.411, 0.435, 0.393, 0.453, 0.404, 0.327, 0.338, \
       0.255, 0.269, 0.217, 0.219, 0.252, 0.278, 0.197, 0.207, 0.337, 0.561, \
       0.223, 0.312, 0.53, 0.652, 0.493, 0.131, 0.16, 0.343, 0.264, 0.178, \
       0.205, 0.221, 0.222, 0.179, 0.206, 0.237, 0.251, 0.24, 0.293, 0.555, \
       0.3, 0.282, 0.332, 0.396, 0.603, 0.515, 0.379, 0.476, 0.433, 0.536, \
       1.0, 0.474, 0.459, 0.471, 0.458, 0.448, 0.465, 0.484, 0.65, 0.494, \
       0.37, 0.358, 0.313, 0.303, 0.29, 0.245, 0.235, 0.322, 0.208, 0.226, \
       0.383, 0.679, 0.231, 0.35, 0.518, 0.806, 0.655, 0.177, 0.238, 0.229, \
       0.431, 0.338, 0.228, 0.219, 0.231, 0.246, 0.285, 0.307, 0.253, 0.347, \
       0.468, 0.331, 0.383, 0.369, 0.379, 0.481, 0.446, 0.685, 0.585, 0.474, \
       0.548, 0.498, 0.907, 0.606, 0.469, 0.462, 0.447, 0.493, 0.51, 0.472, \
       0.467, 0.669, 0.591, 0.396, 0.294, 0.342, 0.39, 0.353, 0.359, 0.368, \
       0.251, 0.32, 0.419, 0.683, 0.23, 0.36, 0.535, 0.819, 0.752, 0.193, \
       0.235, 0.297, 0.259, 0.465, 0.359, 0.209, 0.21, 0.23, 0.264, 0.34, \
       0.451, 0.266, 0.293, 0.346, 0.312, 0.299, 0.311, 0.41, 0.414, 0.692, \
       0.577, 0.487, 0.545, 0.622, 0.95, 0.782, 0.51, 0.532, 0.566, 0.61, \
       0.581, 0.553, 0.558, 0.68, 0.552, 0.35, 0.331, 0.376, 0.434, 0.412, \
       0.343, 0.311, 0.335, 0.318, 0.458, 0.821, 0.315, 0.341, 0.487, 0.954, \
       0.719, 0.293, 0.282, 0.243, 0.291, 0.576, 0.449, 0.25, 0.267, 0.267, \
       0.303, 0.36, 0.279, 0.311, 0.288, 0.425, 0.246, 0.272, 0.297, 0.33, \
       0.339, 0.641, 0.562, 0.4, 0.503, 0.506, 0.667, 0.73, 0.411, 0.418, \
       0.422, 0.471, 0.468, 0.471, 0.449, 0.567, 0.484, 0.332, 0.292, 0.28, \
       0.337, 0.288, 0.275, 0.278, 0.275, 0.294, 0.442, 0.668, 0.179, 0.275, \
       0.377, 0.716]
    
    def __init__(self, pt_from=None, pt_to=None):
        super().__init__()
        self.ts_data = self.beer_data.copy()
        pt_from = 0 if pt_from == None else pt_from
        pt_to = len(self.ts_data)-1 if pt_to == None else pt_to
        self.ts_data = self.ts_data[pt_from:pt_to]
        minv, maxv = min(self.ts_data), max(self.ts_data)
        self.ts_len = len(self.ts_data)
        self.xmin = 0
        self.xmax = self.ts_len-1
        self.ymin = min(self.ts_data)
        self.ymax = max(self.ts_data)
        self.epsilon = 0.1
        
    def fun_point(self, x):
        # print(x)
        if (x < self.xmin):
            return 0.0
        elif (x > self.xmax):
            return 0.0
        elif (int(x) == self.xmax):
            return self.ts_data[-1]
        else:
            lx = int(x)
            ux = lx+1
            ly = self.ts_data[lx]
            uy = self.ts_data[ux]
            return ly+(x-lx)*(uy-ly)/(ux-lx)

    def fun(self, x):
        if type(x) is int or type(x) is float or type(x) is np.float64:
            return self.fun_point(x)
        else:
            return np.array([self.fun_point(xi) for xi in x])

##### Reshape data to allow windowing
#     It leaves a window size gap between training and validation partition
#     - To be fixed in the future

### Converts a flat time series to a windowed set of records
#   - Ignores X coordinates, so points are assumed equidistant
#   y: time series, where indeces are equidistant
#   wind: specific window size
#   step: step between windows
#   returns: a set of sliding windows of y
def y_wind_make(y, wind, step):
    y_wind = np.array([np.array(y[i:i+wind]) for i in range(0, len(y)-wind+1, step)])
    return y_wind

### Converts a flat time series into X and y set of records
#   y: time series, where indeces are equidistant
#   wind: specific window size
#   step: step between windows
#   horizon: the number of future data points to be predicted and used as y, if 0 no prediction
#   returns: sliding windows of X and y
def Xy_wind_make(y, wind, step, horizon):
    full_wind = wind + horizon
    Xy_wind = y_wind_make(y, full_wind, step)
    return Xy_wind[:,:wind], Xy_wind[:,wind:]

### Splits windowed data into training and validation sets
#   y: time series, where indeces are equidistant
#   wind: specific window size
#   step: step between windows
#   horizon: the number of future data points to be predicted and used as y, if 0 no prediction
#   split: percentage of data to be used for training, the rest for validation
#   returns: sliding windows of X and y split into training X, Y and validation X, y
def Xy_wind_split(y, wind, step, horizon, split):
    X, y = Xy_wind_make(y, wind, step, horizon)
    train_size = int(np.round(X.shape[0] * split, 0))
    return X[:train_size], y[:train_size], X[train_size:], y[train_size:]
