from lexpp import Lexpp

pp = Lexpp()

def replace_with_synonynms():

	INPUT = "宛先はこちら"

	# In practical, you must tokenize text into words
	res = INPUT[0:2]

	entry = list(pp.lookup(res))[0]
	synset = pp.get_synset(entry)

	replaced = []
	for syn in synset:
		replaced.append(INPUT.replace(res, syn.surface))

	print(INPUT, "->", replaced)


def normalize_hyokiyure():

	"""
	from synonyms.txt

	000027,1,0,1,0,0,0,(店),漫画喫茶,,
	000027,1,0,1,0,0,2,(店),まんが喫茶,,
	000027,1,0,1,0,0,2,(店),マンガ喫茶,,
	000027,1,0,1,0,2,0,(店),漫喫,,
	000027,1,0,1,0,2,2,(店),まん喫,,
	000027,1,0,1,0,2,2,(店),マン喫,,
	"""

	reference = "漫画喫茶"
	hyokiyure_list = ["まんが喫茶", "マンガ喫茶", "漫喫", "まん喫", "マン喫"]

	print("original:", hyokiyure_list)

	repr_form_list = []

	for i in hyokiyure_list:
		entry = list(pp.lookup(i))[0]
		repr_form = pp.get_representative_form(entry)
		assert(reference == repr_form)
		repr_form_list.append(repr_form)

	print("normalized:", repr_form_list)


def main():
	replace_with_synonynms()
	normalize_hyokiyure()

if __name__ == '__main__':
	main()
