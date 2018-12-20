import vcr


@vcr.use_cassette(
    "fixtures/vcr_cassettes/test_donation_redirect_url.yaml",
    filter_headers=["Authorization", "Idempotency-Key"],
)
def test_donation_middleware_form_valid(db, client):
    form_data = {
        "donation_form-amount": 10,
        "donation_form-payment_type": "subscription",
    }
    req = client.post("/donate/", form_data)
    assert (
        req.url
        == "https://pay-sandbox.gocardless.com/flow/RE0000WH5ETXVTJE5BKT7BS28NNNG8WQ"
    )  # noqa
    assert req.status_code == 302
