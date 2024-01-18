uni_dict_faculties = dict(zip(hk_universities,uni_faculties))
uni_dict_links = dict(zip(hk_universities,uni_links))
def get_faculties(uni):
    for i in hk_universities:
        if uni == i:
            faculties_dict = [uni,uni_dict_faculties.get(uni),uni_dict_links.get(uni)]
    return faculties_dict

def get_profs(faculty, faculty_link):
    return [faculty, " "]

get_profs("School of Science", get_faculties("HKUST")[2])
print (get_faculties("HKUST"))