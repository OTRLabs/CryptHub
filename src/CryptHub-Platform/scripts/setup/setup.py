import os
import subprocess
import podman

CRYPTHUB_COMPONENTS: dict = {

    ## CryptCore ##
    "CryptCore": {
        "name": "CryptCore",
        "description": "CryptHub's core framework.",
        },
    

    ## CryptUI ##
    "CryptUI": {
        "name": "CryptUI",
        "description": "CryptHub's User Interface system built using Vue.",
        },

    ## CryptDB ##
    "CryptDB": {
        "name": "CryptDB",
        "description": "CryptHub's database management system.",
        },

    ## CryptBucket ##
    "CryptBucket": {
        "name": "CryptBucket",
        "description": "CryptHub's storage solution based on Amazon S3.",
    },

    ## CryptFlows ##
    "CryptFlows": {
        "name": "CryptFlows",
        "description": "Task orchestrator handling workflow logic using Directed Acyclic Graphs (DAGs).",
    },

    ## CryptComms ##
    "CryptComms": {
        "name": "CryptComms",
        "description": "CryptHub's comprehensive communication system.",
    },
    
    ## CryptGit ##
    "CryptGit": {
        "name": "CryptGit",
        "description": "CryptHub's Git management system.",
    }
    

}


def breakdown_env_to_each_components_directory():
    
    example_env = "src/CryptHub-Platform/.env.example"
    
    components_directories_directory = "src/CryptHub-Platform/components"

    ## parse each component's env variables, and create a unique .env file for each component within their directory.
    for component in CRYPTHUB_COMPONENTS:

        component_env = f"src/CryptHub-Platform/components/{component}/.env"

        subprocess.run(["cp", example_env, component_env])
        
        ## read the .env file and update its variables
        with open(component_env, "r") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("##"):
                continue
            else:
                key, value = line.strip().split("=")
                value = value.strip()
                new_line = f"{key}={value}\n"
                lines[lines.index(line)] = new_line

        with open(component_env, "w") as f:
            f.writelines(lines)
            
        print(f".env file for {component} has been created.")

    



def main():
    
    ## break each components .env down into individual .env files.
    ## this way, all .env var's are not included in every container. only what is required. 
    breakdown_env_to_each_components_directory()
    

