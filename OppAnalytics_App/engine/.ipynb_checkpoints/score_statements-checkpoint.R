## Basic script that reads in statements and scores them using the engine

# Get command-line arguments (excluding the script name itself)
args = commandArgs(trailingOnly = TRUE)

input_file = args[1]
output_file = sub("\\.csv$", "_processed.csv", input_file)

# Load required libraries
suppressMessages(library(dplyr))
suppressMessages(library(data.table))
suppressMessages(library(glue))

# Read the CSV file
data = fread(input_file)

# Add time for testing the app features
Sys.sleep(30)

# Do a simple transformation: calculate line item-to-assets ratio
data = data %>%
    mutate(liab_asset_ratio = ifelse(assets == 0, NA, liabilities / assets))

# We just overwrite with a generic output file for testing
data = fread("data/sample_statements/sample_output.csv")

# Write the processed output
data %>% fwrite(output_file)