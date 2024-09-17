import argparse
import os
import sys

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
BUILD_SCRIPT = os.path.join(SCRIPT_PATH, "0_build.sh")
RUN_GPU_SCRIPT = os.path.join(SCRIPT_PATH, "1_run_gpu.sh")
RUN_CPU_SCRIPT = os.path.join(SCRIPT_PATH, "1_run_cpu.sh")

# TODO: Make sure this path points to the root of the project
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))


def main():
    parser = argparse.ArgumentParser(description="Submit a job")

    parser.add_argument(
        "--mode",
        dest="mode",
        required=True,
        help="Mode: build, gpu, cpu",
        type=str,
        default="gpu",
    )

    parser.add_argument(
        "--mail",
        dest="mail",
        required=False,
        help="Email",
        type=str,
        default="foo@gmail.com",
    )

    args, unknown = parser.parse_known_args()

    ARGS = " ".join(unknown)
    print("Mode:", args.mode)
    print("Calling with args:", ARGS)

    if args.mode == "build":
        os.system(
            f'sbatch --mail-user={args.mail} {BUILD_SCRIPT} {PROJECT_DIR} "{ARGS}"'
        )
    elif args.mode == "gpu":
        print(f"uv run {ARGS}")
        os.system(
            f'sbatch --mail-user={args.mail} {RUN_GPU_SCRIPT} {PROJECT_DIR} "{ARGS}"'
        )
    elif args.mode == "cpu":
        print(f"uv run {ARGS}")
        os.system(
            f'sbatch --mail-user={args.mail} {RUN_CPU_SCRIPT} {PROJECT_DIR} "{ARGS}"'
        )
    else:
        print("Device not recognized. Please choose gpu or cpu.")
        sys.exit(1)


if __name__ == "__main__":
    main()
