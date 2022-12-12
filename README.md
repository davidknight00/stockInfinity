# StockInfinity

This is an app that will display stocks to users. Users can favorite stocks they want to track and receive real time notifications about price changes.

## Getting Started

To get started with this web app, simply clone this repository and ensure the necessary dependencies are downloaded.

```
git clone https://github.com/davidknight00/stockInfinity/
```

### Requirements

Installing the dependencies can be done as shown below:

```
pip install -r requirements.txt
```

After getting an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key), you will need to insert the API key into the `stockInfinity/stockInf/views.py` file. 

### Tests

Unit testing can be done with the following command:

```
python3 manage.py test stockInf
```

## Deployment

Once the dependencies are successfully downloaded, this web app can be run locally through localhost as so:

```
python3 manage.py runserver
```

## Built With

This app was build with Django (web framework) and Alpha Vantage (API)

## Contributing

Please read [CONTRIBUTING.md](https://www.github.com/davidknight00/stockInfinity/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

**Version: 1.0.0**. We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/davidknight00/stockInfinity). 

## Authors

This app would not be possible without the six original creators: Alex Poole, David Knight, Jack Shanley, Joshua Heinz, Nate Chan, and Preston Lee.
