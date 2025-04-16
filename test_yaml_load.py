# test_yaml_load.py

from src.utils.main_utils import MainUtils

def main():
    utils = MainUtils()
    cfg = utils.read_yaml_file("config/model.yaml")
    models = list(cfg["model_selection"]["model"].keys())
    print("Loaded models from YAML:", models)

if __name__ == "__main__":
    main()
