import os
import tarfile
from six.moves import urllib

def fetch_data(url, path, name):
	if not os.path.isdir(path):
		os.makedirs(path)
		# if not os.path.isfile(path + "/" + name):
		tgz_path = os.path.join(path, name)
		urllib.request.urlretrieve(url, tgz_path)
		# data = tarfile.open(tgz_path)
		# data.extractall(path=path)
		# data.close()
