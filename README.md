# User Transactions Analysis

The goal is to process a file and enrich it with data provided by an API in order to provide high-level aggregate info.

## Description

### API

There are two endpoints: one that searches for the `user_status` on a given date and another one that returns a `city` based on the provided IP.

#### Endpoint user_status
`/user_status/<user_id>?date=2017-10-10T10:00:00`

This endpoint searches the records and returns the correct `user_status` at the given date.
In case there is no status available for a specific date, simply returns `non-paying`.
The valid responses that should be provided are: `paying`, `canceled` or `non-paying`.

#### Endpoint city
`/ip_city/10.0.0.0`
This endpoint searches the provided IP ranges and returns the correct city based on the IP.
In case the IP range is not within any of the provided cities, **unknown** is returned.


## File processing

To generate results:

```
pip install -r requirements.txt
python api.py
python enrichment.py
```
