"""openbb_orats OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider

from openbb_orats.models.tickers import OratsTickersOptionsChainsFetcher

# mypy: disable-error-code="list-item"

orats_provider = Provider(
    name="ORATS",
    description="Data provider for ORATS.",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    # credentials=["api_key"],
    website="https://orats.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Tickers": OratsTickersOptionsChainsFetcher,
    },
)
