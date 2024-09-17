#!/usr/bin/env bash
#SBATCH --job JOB_NAME
#SBATCH --partition=cpu-2h
#SBATCH --cpus-per-task=8        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=3G         # memory per cpu-core (4G per cpu-core is default)
##SBATCH --gpus-per-node=1
#SBATCH --ntasks-per-node=1
#SBATCH --output=logs/JOB_NAME-job-%j.out

PROJECT_DIR=$1
ARGS=$2

cd $PROJECT_DIR
echo "Running: uv --no-cache run $ARGS"
ls -l
apptainer run \
    --env-file ~/.env \
    --nv \
    --writable-tmpfs \
    --bind "$PROJECT_DIR:/workdir" \
    $PROJECT_DIR/cluster/artifacts/apptainerfile.sif "$ARGS"