from accelergy.energy_calculator import EnergyCalculator

import  argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ERT_path', type=str, help = 'path to input file ERT.yaml')
    parser.add_argument('action_counts_path', type=str, help = 'path to input file action_counts.yaml')
    parser.add_argument('-o', '--outdir', type=str, default='./', help = 'optional path to output directory')
    parser.add_argument('-p', '--precision', type=int, default='3', help= 'number of decimal points for energy values' )

    args = parser.parse_args()
    ert_path = args.ERT_path
    action_counts_path = args.action_counts_path
    output_path = args.outdir
    precision = args.precision

    estimator = EnergyCalculator()
    estimator.generate_estimations(action_counts_path, ert_path, output_path, precision)



