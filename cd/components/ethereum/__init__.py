
from kapitan.inputs.helm import HelmChart
from kapitan.inputs.kadet import BaseObj, inventory, load_from_search_paths

inv = inventory()
# utils = load_from_search_paths("utils")  

def main():
    main_obj = BaseObj()

    ethereum = HelmChart(
            chart_dir='charts/ethereum',
            helm_params={"namespace": "local-test", "name": "ethereum-test"},
            helm_values_files='charts/values-files/values.yaml'
            )
    
    main_obj.root.update(ethereum.root)

    return main_obj
