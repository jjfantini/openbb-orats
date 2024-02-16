# openbb-orats Package

## Introduction

The openbb-orats package is a specialized extension designed for the OpenBB Platform, focusing on integrating options data and analytics from ORATS (Options Research & Technology Services). This package serves as a bridge, allowing users to access and manipulate options data seamlessly within the OpenBB Platform environment.

Key features include:

* Retrieving options data including pricing, Greeks, and implied volatility
* Performing advanced options analytics
* Accessing historical options data and trends
* Customizable queries for specific data retrieval

## Getting Started

To effectively utilize the openbb-orats package, familiarize yourself with its core components and functionalities:

* `openbb_orats/router.py` - Defines the routes for data retrieval and analytics commands.
* `openbb_orats/provider.py` - Manages data fetching from ORATS API.
* `openbb_orats/models/` - Contains models for structuring the options data.
* `openbb_orats/__init__.py` - Initializes the package, making it ready for use within the OpenBB Platform.
