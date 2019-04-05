import dill

source_DF = dill.source.getsource(pandas.DataFrame)
print(type(source_DF))
print(len(source_DF))
print(source_DF[:200])

source_file_DF = dill.source.getsourcefile(pandas.DataFrame)
print(source_file_DF)

sourcelines_DF = dill.source.getsourcelines(pandas.DataFrame)
print(type(sourcelines_DF))
print(len(sourcelines_DF))
print(type(sourcelines_DF[0]))

<type 'str'>
195262
