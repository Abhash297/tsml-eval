import os


def run_experiment(dataset_name, data_path, results_path, resample_id):
    command = [
        "python3",
        "/lyceum/as14n23/my_tsml/tsml-eval/tsml_eval/publications/y2023/tsc_bakeoff/run_experiments.py",  # REPLACE WITH THE PATH TO YOUR SCRIPT THE RUNS BAKEOFF
        data_path,
        results_path,
        classifier,
        dataset_name,
        str(resample_id),
        "-nj",
        str(n_jobs),
    ]

    if overwrite:
        command.append("-ow")

    os.system(" ".join(command))


# Parameters
data_base_path = "/lyceum/as14n23/test_Dataset"  # Replace with path to your dataset folder in the HPC
results_base_path = (
    "/lyceum/as14n23/HPC_slurm_op"  # Replace with path to your output folder in the HPC
)
classifier = "STC"
n_jobs = 1
overwrite = True

univariate_datasets = ["ArrowHead"]  # Complete this list based on your datasets

# Example usage
for dataset in univariate_datasets:
    for resample_id in range(5):
        data_path = data_base_path
        results_path = results_base_path
        run_experiment(dataset, data_path, results_path, resample_id)
