class Project:
    def __init__(self, name, project_id):
        self.name = name
        self.project_id = project_id

    def __repr__(self):
        return f"Project(name='{self.name}', project_id='{self.project_id}')"


class Seller:
    def __init__(self, company_name, sales_rep):
        self.company_name = company_name
        self.sales_rep = sales_rep
        self.projects = []  # Will store Project objects

    def add_project(self, project_name, project_id):
        new_project = Project(project_name, project_id)
        self.projects.append(new_project)

    def display_info(self):
        print(f"Company: {self.company_name}")
        print(f"Sales Representative: {self.sales_rep}")
        print("Projects:")
        for project in self.projects:
            print(f"  - {project.name} (SF ID: {project.project_id})")


# Example usage:
sellers = {}

# Create a seller
sellers["SytroSystems Carolinas"] = Seller("SytroSystems Carolinas", "Michael Shafer")

# Add multiple projects
sellers["SytroSystems Carolinas"].add_project("Pyramid", "SF12345")
sellers["SytroSystems Carolinas"].add_project("ATDM II", "SF67890")

# Another seller
sellers["TechWorld"] = Seller("TechWorld", "Jane Smith")
sellers["TechWorld"].add_project("Cloud Migration", "SF11111")

# Display info for Acme Corp
sellers["SytroSystems Carolinas"].display_info()