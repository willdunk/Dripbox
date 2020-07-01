def removeNonReviews(entries):
	return filter(lambda entry: 'letterboxd-review' in entry.id, entries)
