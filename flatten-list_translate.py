#if sys.version_info[0]>=3:
if 'maketrans' in str.__dict__:
	maketrans=str.maketrans
else:
	from string import maketrans
flat_list=lambda a:eval('['+str(a).translate(maketrans('','','[]'))+']')