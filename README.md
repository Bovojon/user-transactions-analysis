# Data Engineer Task

For the assignment, you have to process a file and enrich it with data provided by an API in order to provide high-level aggregate info.

Our goal is to see how you implement the missing parts of the API and how you deal with file processing and data structures manipulation.

As we use to containerize our applications please add a Dockerfile for running the api.

## Description

### API

There are two endpoints that need to be implemented, one that searches for the `user_status` on a given date and another one that returns a `city` based on the provided IP.

#### Endpoint user_status
`/user_status/<user_id>?date=2017-10-10T10:00:00`

On this endpoint please provide an implementation that searches the records and returns the correct `user_status` at the given date.
In case there is no status available for a specific date, simply return `non-paying`.
The valid responses that should be provided are: `paying`, `canceled` or `non-paying`.

#### Endpoint city
`/ip_city/10.0.0.0`
On this endpoint please provide an implementation that searches the provided IP ranges and returns the correct city based on the IP.
In case the IP range is not within any of the provided cities, **unknown** should be returned.

### File Processing

Please read the file `transactions.json` and enrich it with the data given by the API.
The output of the script should provide an aggregate containing the sum of `product_price` grouped by `user_status` and `city`.

## Setup

There is a simple API which you'll need to install.
To run the API just run the api.py file.

```
pip install -r requirements.txt
python api.py
```


### Delivery

Please provide a zip or tar file containing your complete implementation.
# user-transactions-analysis


## Test

Open a terminal and run the following:
```
pip install -r requirements.txt
python api.py
```
Open another terminal and run the following to generate the final aggregate result and the enriched transactions:
```
python enrichment.py
```