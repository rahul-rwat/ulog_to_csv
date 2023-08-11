# uLog to CSV Converter

!https://img.shields.io/badge/python-3.x-blue.svg

!https://img.shields.io/badge/license-MIT-green.svg

The uLog to CSV Converter is a Python script that allows you to easily convert uLog files to CSV format, making it convenient for data analysis. uLog files are commonly used in the field of robotics and embedded systems to log data from various sensors and components. Converting them to CSV format can simplify the process of data manipulation and analysis using popular tools like Excel, pandas, and more.

## Features

- Converts uLog files to CSV format.
- Supports various uLog file versions.
- Preserves the structure of the data for easy analysis.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository to your local machine or download the ZIP file and extract it.
    
    ```bash
    git clone https://github.com/rahul-rwat/ulog_to_csv.git
    
    ```
    
2. Navigate to the project directory.
    
    ```bash
    cd ulog_to_csv
    ```
    
3. Install the required dependencies.
    
    ```bash
    pip install -r requirements.txt
    
    ```
    

### Usage

1. Place your uLog file (with a `.ulg` extension) in the same directory as the `ulog_to_csv.py` script. Name the file as  `ulog.ulg` .
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the conversion script by executing the following command:
    
    ```bash
    python ulog.py 
    ```
    
    Replace `your_log_file.ulg` with the actual name of your uLog file.
    
4. The converted CSV file will be generated in the same directory with the same name as the input uLog file but with a `.csv` extension.

## License

This project is licensed under the MIT License - see the [LICENSE](notion://www.notion.so/LICENSE) file for details.

## Acknowledgments

- This script utilizes the [pyulog](https://github.com/PX4/pyulog) library to parse uLog files.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a GitHub issue or pull request in this repository.
