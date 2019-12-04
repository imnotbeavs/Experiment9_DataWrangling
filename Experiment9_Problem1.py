import pandas as pd
math = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'Math':[80, 95, 79]}
elecs = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'Electronics':[85, 81, 83]}
geas = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'GEAS':[90, 79, 93]}
esat = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'ESAT':[93, 89, 88]}

math = pd.DataFrame(math, columns = ['Student','Math'])
elecs = pd.DataFrame(elecs, columns = ['Student','Electronics'])
geas = pd.DataFrame(geas, columns = ['Student','GEAS'])
esat = pd.DataFrame(esat, columns = ['Student','ESAT'])


merge = pd.merge(pd.merge(pd.merge(math,elecs, on='Student'),geas, on = 'Student'),esat, on = 'Student')
long_format =pd.melt(merge, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
long_format = long_format.rename(columns = {'variable' : 'Subject', 'value' : 'Grades'})
long_format = long_format.sort_values('Student').reset_index().drop(columns = 'index')
