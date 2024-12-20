import yaml
class ConfigLoader:
     
     def __init__(self,config_file_path:str) -> None:
        self.config = self.load_settings(config_file_path)

     def load_settings(self,config_file_path:str):
            with open(config_file_path, "r") as file:
                config = yaml.safe_load(file)
            return config
     
     def return_step_config(self,key:str) -> dict:
        return self.config[key]