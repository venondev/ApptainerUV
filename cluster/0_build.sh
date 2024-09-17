#!/usr/bin/env bash
#SBATCH --job JOB_NAME
#SBATCH --partition=cpu-test
#SBATCH --cpus-per-task=8        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=3G         # memory per cpu-core (4G per cpu-core is default)
##SBATCH --gpus-per-node=1
#SBATCH --ntasks-per-node=1
#SBATCH --output=logs/JOB_NAME-job-%j.out

PROJECT_DIR=$1

echo Building apptainer container for project dir: $PROJECT_DIR
apptainer build --fakeroot --force $PROJECT_DIR/cluster/artifacts/apptainerfile.sif $PROJECT_DIR/cluster/apptainerfile.def