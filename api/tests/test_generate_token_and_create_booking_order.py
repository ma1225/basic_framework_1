from api.api_impl.auth_token_impl import AuthTokenImpl
from api.api_impl.booking_management_impl import BookingManagementImpl
from utils.helpers.random_generator import *
from logging import getLogger
import json

logger = getLogger(__name__)

def test_generate_token_and_create_booking_order():

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
    assert response["booking"]["lastname"] == order_last_name, logger.error(f"Booking order last name is wrong! "
                                                                            f"Actual: '{response["booking"]["lastname"]}' "
                                                                            f"but Expected is: '{order_last_name}'!")
    assert response["booking"]["totalprice"] == order_price, logger.error(f"Booking order total price is wrong! "
                                                                          f"Actual: '{response["booking"]["totalprice"]}' "
                                                                          f"but Expected is: '{order_price}'!")
    booking_id = response["bookingid"]

    logger.info("Get new booking order by booking order ID and verify data with API call")
    response, status = booking_manage_impl.get_booking_order_by_booking_id(auth_token, booking_id)
    assert status, logger.error("Failed to get new booking order by ID!")

    logger.info(f"Order ID '{str(booking_id)}' info: {json.dumps(response)}")
    assert response["firstname"] == order_first_name, logger.error(f"Booking order first name is wrong! "
                                                                   f"Actual: '{response["firstname"]}' "
                                                                   f"but Expected is: '{order_first_name}'!")
    assert response["lastname"] == order_last_name, logger.error(f"Booking order last name is wrong! "
                                                                 f"Actual: '{response["lastname"]}' "
                                                                 f"but Expected is: '{order_last_name}'!")
    assert response["totalprice"] == order_price, logger.error(f"Booking order total price is wrong! "
                                                               f"Actual: '{response["totalprice"]}' "
                                                               f"but Expected is: '{order_price}'!")
