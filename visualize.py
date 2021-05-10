import pandas as pd
corespeed = pd.read_table('test.txt', sep='\t', header=None, encoding='utf-16' \
                          ,names = ['MHz'])
corespeed.plot(figsize=(20,3))
