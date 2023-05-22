import os
import csv
import requests
import datetime


def fetch_repo_info(repo_name, user_name):
    """Fetches information about a GitHub repository.

    Args:
        repo_name (str): The name of the repository.
        user_name (str): The username of the owner of the repository.

    Returns:
        dict: A dictionary containing information about the repository, or None if the repository could not be found.
    """

    url = f"https://api.github.com/repos/{user_name}/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info
    else:
        return None


def process_csv(input_csv, output_folder):
    """Processes a CSV file containing information about GitHub repositories.

    Args:
        input_csv (str): The path to the input CSV file.
        output_folder (str): The path to the output folder.

    Returns:
        tuple: The path to the output CSV file, and the path to the log file.
    """

    output_csv = os.path.join(output_folder, "output.csv")
    log_file = os.path.join(output_folder, "log.txt")

    with open(input_csv, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        valid_entries = []
        for row in csv_reader:
            if len(row) == 2:
                repo_name, user_name = row
                valid_entries.append((repo_name, user_name))

    with open(output_csv, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Repo Name", "User Name", "Stars", "Forks", "URL"])
        with open(log_file, "w") as log:
            for repo_name, user_name in valid_entries:
                log.write(f"{datetime.datetime.now()}: Fetching info for {user_name}/{repo_name}\n")
                repo_info = fetch_repo_info(repo_name, user_name)
                if repo_info:
                    stars = repo_info["stargazers_count"]
                    forks = repo_info["forks_count"]
                    url = repo_info["html_url"]
                    csv_writer.writerow([repo_name, user_name, stars, forks, url])
                    log.write(f"{datetime.datetime.now()}: Successfully processed {user_name}/{repo_name}\n")
                else:
                    log.write(f"{datetime.datetime.now()}: Failed to process {user_name}/{repo_name}\n")

    return output_csv, log_file


def main():
    input_csv = input("Enter the path to the input CSV file: ")
    output_folder = input("Enter the path to the output folder: ")

    output_csv, log_file = process_csv(input_csv, output_folder)
    print(f"Output CSV file saved to: {output_csv}")
    print(f"Log file saved to: {log_file}")

if __name__ == "__main__":
    main()

