import hashlib

BLOCK_SIZE = 65536  # The size of each read from the file

def get_digest(file):
	file.seek(0)
	# Create the hash object, can use something other than `.sha256()` if you wish
	file_hash = hashlib.sha256()
	fb = file.read(BLOCK_SIZE)
	while len(fb) > 0:  # While there is still data being read from the file
		file_hash.update(fb)  # Update the hash
		fb = file.read(BLOCK_SIZE)  # Read the next block from the file
	file.seek(0)
	return file_hash.hexdigest()

def get_name(file):
	return ''.join(file.filename.split(".")[:-1])

def get_extension(file):
	return file.filename.split(".")[-1]