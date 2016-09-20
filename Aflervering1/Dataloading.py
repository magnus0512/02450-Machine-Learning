"""
@author: Magnus
"""

import numpy as np
import xlrd

# Load xls sheet with data
doc = xlrd.open_workbook('housing.xls').sheet_by_index(0)

# Extract attribute names
attributeNames = doc.row_values(1,0,14)

# Extract class names to python list,
# then encode with integers (dict)
classLabels = doc.col_values(14,2,508)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames,range(6)))

# Extract vector y, convert to NumPy matrix and transpose
y = np.mat([classDict[value] for value in classLabels]).T

# Preallocate memory, then extract excel data to matrix X
X = np.mat(np.empty((506,14)))
for i, col_id in enumerate(range(0,14)):
    X[:,i] = np.mat(doc.col_values(col_id,2,508)).T

# Compute values of N, M and C.
N = 506
M = len(attributeNames)
C = len(classNames)
