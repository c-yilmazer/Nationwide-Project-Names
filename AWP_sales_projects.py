import webbrowser


class Project:
    def __init__(self, name, project_id, sales_rep):
        self.name = name
        self.project_id = project_id
        self.sales_rep = sales_rep #Sales rep's full name

    def __repr__(self):
        return (f"Project(name='{self.name}', project_id='{self.project_id}', sales_rep='{self.sales_rep}')")
    
    
class Company:
    def __init__(self, name):
        self.name = name
        self.sales_reps = set()  # Track unique sales rep names
        self.projects = []       # All projects under this company

    def add_project(self, project_name, project_id, sales_rep):
        self.sales_reps.add(sales_rep)
        new_project = Project(project_name, project_id, sales_rep)
        self.projects.append(new_project)

    def display_info(self):
        print(f"Company: {self.name}")
        print(f"Sales Representatives: {', '.join(self.sales_reps)}")
        print("Projects:")
        for p in self.projects:
            print(f"  - {p.name} (SF ID: {p.project_id}), Sales Rep: {p.sales_rep}")   

companies={}
# Create company
companies["SytroSystem Carolinas"]=Company("Sytrosystem Carolinas")
# Add projects linked to sales reps
companies["SytroSystem Carolinas"].add_project("Pyramid Healthcare", "SF - 006Uz00000XQWxLIAX", "Michael Shafer")
print(Company("SytroSystem Carolinas"))

#Project("Pyramid", "006Uz00000XQWxLIAX", "Michael")
#webbrowser.open_new_tab(f"https://ps-crm-dupont.lightning.force.com/lightning/r/Opportunity/{project_id}/view")

#project_id = "006Uz00000XQWxLIAX"
#print(f"https://ps-crm-dupont.lightning.force.com/lightning/r/Opportunity/{project_id}/view")
#webbrowser.open_new_tab(f"https://ps-crm-dupont.lightning.force.com/lightning/r/Opportunity/{project_id}/view")









#project_id = "006Uz00000XQWxLIAX"
#print(f"https://ps-crm-dupont.lightning.force.com/lightning/r/Opportunity/{project_id}/view")
#webbrowser.open_new_tab(f"https://ps-crm-dupont.lightning.force.com/lightning/r/Opportunity/{project_id}/view")