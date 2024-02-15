"""Example Data Integration.

The OpenBB Platform gives developers easy tools for integration.

To use it, developers should:
1. Define the request/query parameters.
2. Define the resulting data schema.
3. Define how to fetch raw data.

First 2 steps make sure developers really get to know their data.
This is called the "Know Your Data" principle.

Note: The format of the QueryParams and Data is defined by a pydantic model that can
be entirely custom, or inherit from the OpenBB standardized models.

This file shows an example of how to integrate data from a provider.
"""
# pylint: disable=unused-argument
from typing import Any, Dict, List, Optional

import requests
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.options_chains import OptionsChainsQueryParams
from pydantic import Field


class OratsTickersOptionsChainsQueryParams(OptionsChainsQueryParams):
    """ORATS Tickers Query Parameters.

    The QueryParams used in the `/datav2/tickers` endpoint for ORATS.
    We are only interested in the `ticker` QueryParam.
    """


class OratsTickersOptionsChainsData(Data):
    """Sample provider data.

    The fields are displayed as-is in the output of the command. In this case, its the
    Open, High, Low, Close and Volume data.
    """

    ticker: str = Field(description="Ticker symbol.")
    min: str = Field(description="Minimum date in YYYY-MM-DD format.")
    max: str = Field(description="Maximum date in YYYY-MM-DD format.")


class OratsTickersOptionsChainsFetcher(
    Fetcher[
        OratsTickersOptionsChainsQueryParams,
        List[OratsTickersOptionsChainsData],
    ]
):
    """Example Fetcher class.

    This class is responsible for the actual data retrieval.
    """

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> OratsTickersOptionsChainsQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return OratsTickersOptionsChainsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: OratsTickersOptionsChainsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        api_key = credentials.get("openbb_orats_api_key") if credentials else ""

        ORATS_BASE_URL: str = "https://api.orats.io/datav2/"

        urls: str = ORATS_BASE_URL
        urls += "ticker"
        urls += f"?token={api_key}&ticker={query.symbol}"

        res = requests.get(urls, timeout=10)

        return res

    @staticmethod
    def transform_data(
        query: OratsTickersOptionsChainsQueryParams, data: List[dict], **kwargs: Any
    ) -> List[OratsTickersOptionsChainsData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [OratsTickersOptionsChainsData(**d) for d in data]
