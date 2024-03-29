
![logo](https://gitlab.com/uploads/-/system/project/avatar/54594885/_dd2e55ed-f7d2-492e-85ab-1fc802388598.jpg?width=96)
# Better Norminette - Colors in 42 norminette output

`betternom` is a Python utility designed to enhance the output of the norminette by adding colorization to its output, making it easier to distinguish between various types of messages such as errors and successful checks. It utilizes `colorama` for terminal color output and provides additional functionality such as minimizing output and showing errors only.

## Features

- **Colorized Output:** Makes it easier to read norminette outputs by color-coding messages.
- **Minimize Output:** Option to show a minimized version of the output for a quicker overview.
- **Error Only Mode:** Can be configured to show only errors, omitting the OK messages for cleaner output.
- **Summary View:** Provides a summary of the norminette run, including counts of files checked, errors found, etc.

Want another feature ? Ask it to me !

![image info](screenshots/screenshot1.png)

## How to Install

### Prerequisites

Before installing `betternom`, ensure you have Python installed on your system. `betternom` requires Python 3.6 or newer.

### Installation Options

#### Install from GitLab

To install `betternom` directly from the GitLab repository:

1. Clone the repository:

```sh
git clone https://gitlab.com/theo_vdml/betternorm
```

2. Navigate to the cloned directory:

```sh
cd betternom
```

3. Install the package:

```sh
pip3 install .
```

4. If you face an error with permission (at school for example) try with the --user params

```sh
pip3 install . --user
```

This method is useful if you want to install the most recent changes that may not yet be published on PyPI.

## Usage

To use `betternom`, run the following command in your terminal:

```sh
betternorm [filename] [options]
```

Options include:

- `-e`, `--error-only` to display only errors.
- `-m`, `--minimize` for minimized output.
- `-s`, `--summary-only` to display only the summary.
- `-a`, `--args` to pass additional arguments to norminette. (will take the rest of the command line and pass it to norminette)

For detailed help and more options, run:

```sh
betternorm --help
```

## Contributing

We welcome contributions! If you would like to contribute to the project, please fork the repository, make your changes, and submit a merge request on GitLab.

## License

`betternom` is open-source software licensed under the MIT license.
