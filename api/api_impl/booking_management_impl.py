from api.api_calls.booking_management import BookingManagementCalls
from logging import getLogger

logger = getLogger(__name__)


class BookingManagementImpl:

    def __init__(self):
        pass

    @staticmethod
    def create_booking_order(auth_token: str, first_name: str, last_name: str, total_price: int, deposit_paid: bool, check_in_date: str,
                             check_out_date: str, additional_needs: str):

        status = False
        response_json = ""
        booking_management = BookingManagementCalls()

        try:
            logger.info("Create new booking order with API")
            response = booking_management.post_booking_order_call(auth_token=auth_token, first_name=first_name, last_name=last_name, total_price=total_price,
                                                                  deposit_paid=deposit_paid, check_in_date=check_in_date,
                                                                  check_out_date=check_out_date, additional_needs=additional_needs)
            response_json = response.json()
            if response.ok and response_json:
                status = True

        except Exception as e:
            logger.error(f"Error in calling create booking order API with: {e}")

        return response_json, status
