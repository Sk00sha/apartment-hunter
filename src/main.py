from Extract import Extractor
from ConfigLoader import ConfigLoader

if __name__ == "__main__":
    c = ConfigLoader("../config/configuration.yaml")
   
    e = Extractor(c.return_step_config("scraper"))