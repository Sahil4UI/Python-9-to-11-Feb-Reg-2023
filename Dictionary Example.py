#store the details of 5 students in a dictionary along with 3 subject marks,
#then calc avg,grade


x = [{"roll":101,"name":"Ravi","phy":98,"chem":96,"maths":100},
     {"roll":102,"name":"Shyam","phy":68,"chem":70,"maths":65},
     {"roll":103,"name":"Rohit","phy":56,"chem":45,"maths":30},
     {"roll":104,"name":"Yash","phy":8,"chem":6,"maths":10},
     {"roll":105,"name":"Lokesh","phy":100,"chem":100,"maths":100}]


for i in x:
    avg = (i["phy"]+i["chem"]+i["maths"])/3
    
    print(i.get("roll"),i.get("name"),avg)
    
