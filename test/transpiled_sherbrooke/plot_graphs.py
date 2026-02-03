from pandas import read_csv
from matplotlib import pyplot
from pathlib import Path

results_path = 'test/transpiled_sherbrooke/minimum_eigensolvers/results/test_qaoa'
test_cases = [
    ['test_change_operator_size', 1],
    ['test_optimizer_scipy_callable', 1],
    ['test_qaoa_initial_point', 3],
    ['test_qaoa_qc_mixer_many_parameters', 1],
    ['test_qaoa_qc_mixer_no_parameters', 1],
    ['test_qaoa_qc_mixer', 2],
    ['test_qaoa_random_initial_point', 1],
    ['test_qaoa', 2]
]
def main():
    for test_case, iterations in test_cases:
        if iterations > 1:
            for i in range(iterations):
                path_1 = f'{results_path}/{test_case}-ideal_sampler-{i + 1}.csv'
                path_2 = f'{results_path}/{test_case}-sampler_without_noise-{i + 1}.csv'
                path_3 = f'{results_path}/{test_case}-sampler_with_noise-{i + 1}.csv'
                dataframe_1 = read_csv(path_1, header=None)
                dataframe_2 = read_csv(path_2, header=None)
                dataframe_3 = read_csv(path_3, header=None)

                x_col = 0
                for y_col in range(1, len(dataframe_1.columns) - 1):
                    _, axis = pyplot.subplots()

                    axis.plot(dataframe_1[x_col], dataframe_1[y_col], label='Ideal Sampler', color='blue')
                    axis.plot(dataframe_2[x_col], dataframe_2[y_col], label='Sampler without Noise', color='orange')
                    axis.plot(dataframe_3[x_col], dataframe_3[y_col], label='Sampler with Noise', color='green')
                    axis.legend()

                    graph_path = Path(f"{results_path}/graphs/{test_case}/{test_case}-{i + 1}_col-{y_col}.png")
                    graph_path.parent.mkdir(parents=True, exist_ok=True)
                    pyplot.savefig(graph_path)
                    pyplot.close()

        else:
            path_1 = f'{results_path}/{test_case}-ideal_sampler.csv'
            path_2 = f'{results_path}/{test_case}-sampler_without_noise.csv'
            path_3 = f'{results_path}/{test_case}-sampler_with_noise.csv'
            dataframe_1 = read_csv(path_1, header=None)
            dataframe_2 = read_csv(path_2, header=None)
            dataframe_3 = read_csv(path_3, header=None)

            x_col = 0

            for y_col in range(1, len(dataframe_1.columns) - 1):
                _, axis = pyplot.subplots()

                axis.plot(dataframe_1[x_col], dataframe_1[y_col], label='Ideal Sampler', color='blue')
                axis.plot(dataframe_2[x_col], dataframe_2[y_col], label='Sampler without Noise', color='orange')
                axis.plot(dataframe_3[x_col], dataframe_3[y_col], label='Sampler with Noise', color='green')
                axis.legend()

                graph_path = Path(f"{results_path}/graphs/{test_case}/{test_case}_col-{y_col}.png")
                graph_path.parent.mkdir(parents=True, exist_ok=True)
                pyplot.savefig(graph_path)
                pyplot.close()               


if __name__ == "__main__":
    main()
