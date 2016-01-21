from myblog.models import Entity, Subject
import sys, csv

f = open('Database csv_2.csv', 'rt')
reader = csv.reader(f)

test_cnt = 0
for row in reader:
	test_cnt += 1
	if test_cnt == 1:
		continue

	print "Raw name", row[0].strip()
	print "Raw info", row[1].strip()
	print "Raw subj", row[2].strip()

	name = unicode(row[0].strip(), "utf-8")
	short_info = unicode(row[1].strip(), "utf-8")
	subject_list = [unicode(subject.strip(), "utf-8") for subject in row[2].strip().split(',')]
	'''
	name = unicode(row[0].strip(), "utf-8")
	short_info = unicode(row[1].strip(), "utf-8")
	subject_list = [unicode(subject, "utf-8") for subject in row[2].strip()]
	'''
	print subject_list
	# convert subject_list to pk
	subject_list = [Subject.objects.get_or_create(name=subject)[0].id for subject in subject_list]
	#print name, short_info, subject_list

	a = Entity.objects.create(name=name, short_info=short_info)
	a.subjects.add(*subject_list)
	a.save()

print "Total", test_cnt

