# Single original project with SalesForce_ID
project = {"Project Name": {"SalesForce_ID": 10}}

# Full list of 50 US states
us_states = [
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
    "Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa",
    "Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan",
    "Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire",
    "New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",
    "Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
    "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia",
    "Wisconsin","Wyoming"
]

# Build dictionary with each state containing the project nested
state_projects = {state: {project_name: info.copy() for project_name, info in project.items()} 
                  for state in us_states}

# Print first 50 states for brevity, change [:51] to increase or decrease auto generated list
for state, proj in list(state_projects.items())[:51]:
    print(f"{state}: {proj}")



# If you wanted to add more projects to a state New project dictionary
#new_project = {"SalesForce_ID": 20}

# Add it under California
#state_projects["California"]["Project X"] = new_project

# Print California to verify
#print(state_projects["California"])
#Output:


#{'Project Name': {'SalesForce_ID': 10}, 'Project X': {'SalesForce_ID': 20}}