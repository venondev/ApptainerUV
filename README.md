# UV on apptainer

This repository contains scripts and instructions on how to run uv on apptainer on a SLURM cluster like [HYDRA](https://git.tu-berlin.de/ml-group/hydra/documentation).

# Steps

1. Copy the `cluster` folder to the root of your project (for other locations, you need to adjust the paths in the scripts in the `cluster` folder)
2. On the cluster, run

```
python3 cluster/submit_job.py --mode build
```

3. To start a job, run

```
python3 cluster/submit_job.py --mode=gpu /path/to/your/script.py --args ...
```

This will call `uv run /path/to/your/script.py --args ...` in the apptainer container.

# Other scripts

`scripts/taill.sh` can be used to tail the latest log file in a folder.

```
./scripts/taill.sh /path/to/your/log_folder
```
