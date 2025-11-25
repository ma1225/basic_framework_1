from api.api_impl.auth_token_impl import AuthTokenImpl
from api.api_impl.booking_management_impl import BookingManagementImpl
from logging import getLogger
from utils.helpers.random_generator import *
import json

logger = getLogger(__name__)

def test_generate_token_and_create_booking():

    auth_token_impl = AuthTokenImpl()
    booking_manage_impl = BookingManagementImpl()

    logger.info("Generate new auth token for API usage")
    auth_token, status = auth_token_impl.generate_auth_token_for_apis()
    assert status, logger.error("Failed to generate new auth token!")

    logger.info("Create new booking order")
    order_first_name = generate_random_string(10)
    order_last_name = generate_random_string(10)
    order_price = generate_random_integer(1000, 50000)
    deposit_paid = select_random_boolean()
    check_in_date = generate_random_date_string("2025-11-01", "2025-11-23")
    check_out_date = generate_random_date_string("2025-11-24", "2025-12-29")
    additional_needs = generate_random_string(5)
    response, status = booking_manage_impl.create_booking_order(auth_token, order_first_name, order_last_name, order_price,
                                                                deposit_paid, check_in_date, check_out_date, additional_needs)
    assert status, logger.error("Failed to create new booking order!")
    logger.info(f"Order info: {json.dumps(response)}")
    assert response["booking"]["firstname"] == order_first_name, logger.error(f"Booking order first name is wrong! "
                                                                              f"Actual: '{response["booking"]["firstname"]}' "
                                                                              f"but Expected is: '{order_first_name}'!")
