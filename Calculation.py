from sklearn import preprocessing
from scipy.spatial import distance
import numpy as np
import pandas as pd
import xlsxwriter

data = {'X': np.array([31., 15., 36., 22., 15., 50., 22., 37., 24., 17., 42., 50., 20., 40., 37.]),
        'Y': np.array([44., 50., 37., 14., 45., 18., 18., 31., 28., 31., 8., 23., 27., 28., 47.]),
        'Z': np.array([41., 49., 39., 16., 28., 24., 28., 19., 31., 15., 27., 28., 41., 21., 38])}

data_frame = pd.DataFrame(data)
normalized_X = preprocessing.normalize(data_frame)
euclidean_ = distance.cdist(normalized_X, normalized_X, 'euclidean')
cityblock_ = distance.cdist(normalized_X, normalized_X, 'cityblock')
sqeuclidean_ = distance.cdist(normalized_X, normalized_X, 'sqeuclidean')
seuclidean_ = distance.cdist(normalized_X, normalized_X, 'seuclidean', V=None)
workbook = xlsxwriter.Workbook('CP_2.xlsx')
array_ = [euclidean_, cityblock_, sqeuclidean_, seuclidean_]

for i in array_:
        print(i)
        worksheet = workbook.add_worksheet()
        row = 1
        for col, data in enumerate(i):
                worksheet.write_column(row, col, data)

workbook.close()