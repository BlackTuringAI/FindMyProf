hk_universities = ("HKU", "HKUST", "CUHK", "CityU", "PolyU", "HKBU", "LU")
# faculties in uni would not change in short period of time, therefore manually input initial version
hku_faculties = ("Faculty of Architecture", "Faculty of Arts", "Faculty of Business and Economics",
                 "Faculty of Dentistry", "Faculty of Education", "Faculty of Engineering", "Faculty of Law",
                 "Li Ka Shing Faculty of Medicine", "Faculty of Science", "Faculty of Social Sciences")
hkust_faculties = ("School of Science", "School of Engineering", "School of Business and Management",
                   "School of Humanities and Social Science", "Academy of Interdisciplinary Studies")
cuhk_faculties = ("Faculty of Arts", "Faculty of Business Administration", "Faculty of Education",
                  "Faculty of Engineering", "Faculty of Law", "Faculty of Medicine", "Faculty of Science",
                  "Faculty of Social Science")
cityu_faculties = ("College of Business", "College of Liberal Arts and Social Sciences",
                   "Jockey Club College of Veterinary Medicine and Life Sciences", "School of Data Science",
                   "School of Law", "College of Engineering", "College of Science", "School of Creative Media",
                   "School of Energy and Environment")
polyu_faculties = ("Faculty of Business", "Faculty of Construction and Environment", "Faculty of Engineering",
                   "Faculty of Health and Social Sciences", "Faculty of Humanities", "Faculty of Science",
                   "School of Design", "School of Fashion and Textiles", "School of Hotel and Tourism Management")
hkbu_faculties = ("Faculty of Arts", "School of Business", "School of Chinese Medicine", "School of Communication",
                  "School of Creative Arts", "Faculty of Science", "Faculty of Social Sciences",
                  "School of Continuing Education")
lu_faculties = ("Faculty of Arts", "Faculty of Business", "Faculty of Social Sciences")
uni_faculties = (hku_faculties, hkust_faculties, cuhk_faculties, cityu_faculties, polyu_faculties,
                 hkbu_faculties, hkbu_faculties, lu_faculties)

hku_links = ("https://www.arch.hku.hk/people/arch_staff/#academic-staff",
             "https://www.scifac.hku.hk/people", " ")
hkust_links = ("https://facultyprofiles.hkust.edu.hk/facultylisting.php",)
cuhk_links = (" ",)
cityu_links = ("https://www.cityu.edu.hk/directories/people/academic",)
polyu_links = (" ",)
hkbu_links = (" ",)
lu_links = (" ", )
uni_links = (hku_links, hkust_links, cuhk_links, cityu_links, polyu_links, hkbu_links, hkbu_links, lu_links)

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