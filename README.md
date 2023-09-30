# Bank Branches API

This project is a Python web API service built with Flask that supports GraphQL queries for retrieving bank branch data from a CSV file.

## API Purpose

The purpose of this API is to provide access to information about bank branches. It allows users to query and retrieve data about various bank branches using GraphQL queries.

## Endpoints

- The API is hosted on Flask, and the GraphQL endpoint is available at `/gql`. Users can send GraphQL queries to this endpoint.

## Data Source

- The API reads data from a CSV file named `bank_branches.csv`. This file contains information about bank branches, including IFSC codes, branch names, bank names, addresses, cities, districts, states, and more.

## GraphQL Queries

- Users can use GraphQL queries to request specific data about bank branches. An example query is provided below:

   ```graphql
   query {
       branches {
           edges {
               node {
                   branch
                   bank {
                       name
                   }
                   ifsc
               }
           }
       }
   }

This query requests information about bank branches, including the branch name, the name of the bank it belongs to, and the IFSC code.

## Code Implementation
- The implementation is based on Flask and Flask-GraphQL, which is a Flask extension for creating GraphQL APIs.
- Code snippets for loading data from the CSV file and returning it as a GraphQL response have been provided.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (version 3.6 or higher) installed on your system.
- Python virtual environment set up.

# Installation

1. **Clone this repository to your local machine:**

   ```shell
   git clone https://github.com/theakashshukla/bank-api.git
   ```

2. **Navigate to the project folder:**

   ```shell
   cd bank-api
   ```

3. **Create a virtual environment:**

   ```shell
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```shell
     source venv/bin/activate
     ```

5. **Install the required Python packages:**

   ```shell
   pip install -r requirements.txt
   ```

   OR

   ```shell
   pip install Flask Flask-GraphQL graphene
   ```

## Usage

1. **Start the Flask app:**

   ```shell
   python app.py
   ```

   The app will run at `http://localhost:5000`.

2. **Open a web browser and navigate to `http://localhost:5000/gql`.** This will open the GraphiQL interface.

3. **Use the GraphiQL interface to execute GraphQL queries to retrieve bank branch data.**

   Sample GraphQL Query:

   ```graphql
   query {
     branches {
       ifsc
       branch
       bank
     }
   }
   ```

   Press the "Play" button to execute the query and view the results.

## Data Loading

The data loading logic in `app.py` reads data from the `bank_branches.csv` file. Ensure that the CSV file is located in the same directory as `app.py` and follows the correct format:

```
ifsc,bank_id,branch,address,city,district,state,bank_name
```

## Contributing

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your fork.
- Submit a pull request to the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

```
