from api.api_calls.booking_management import BookingManagementCalls
from logging import getLogger

logger = getLogger(__name__)


class BookingManagementImpl:

    def __init__(self):
        pass

    @staticmethod
    def create_booking_order(auth_token: str, first_name: str, last_name: str, total_price: int, deposit_paid: bool, check_in_date: str,
                             check_out_date: str, additional_needs: str):
        """
        :param auth_token: Auth token needed for sending the API request
        :param first_name: First name of customer on order
        :param last_name: Last name of customer on order
        :param total_price: Total price of the booking order
        :param deposit_paid: True or False if the deposit was paid
        :param check_in_date: Check in start date
        :param check_out_date: Check out end date
        :param additional_needs: Additional customer needs if was filled
        :return: API response JSON after it was validated for 200 OK with booking order info and API status
        """
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

    @staticmethod
    def get_all_booking_orders(auth_token: str, wildcard_params: str = None):
        """
        :param auth_token: Auth token needed for sending the API request
        :param wildcard_params: Wildcard parameters in API request (for example: "firstname=sally&lastname=brown")
        :return: API response JSON after it was validated for 200 OK with all booking order info exist and API status
        """

        status = False
        response_json = ""
        booking_management = BookingManagementCalls()

        try:

            logger.info("Create new booking order with API")
            response = booking_management.get_all_booking_orders_call(auth_token=auth_token, wildcard_params=wildcard_params)
            response_json = response.json()
            if response.ok and response_json:
                status = True

        except Exception as e:
            logger.error(f"Error in calling get all booking order API with: {e}")

        return response_json, status

    @staticmethod
    def get_booking_order_by_booking_id(auth_token: str, booking_id: int):
        """
        :param auth_token: Auth token needed for sending the API request
        :param booking_id: ID of the booking order
        :return: API response JSON after it was validated for 200 OK with specific booking order by ID info and API status
        """

        status = False
        response_json = ""
        booking_management = BookingManagementCalls()

        try:

            logger.info("Create new booking order with API")
            response = booking_management.get_booking_order_by_id_call(auth_token=auth_token, booking_id=booking_id)
            response_json = response.json()
            if response.ok and response_json:
                status = True

        except Exception as e:
            logger.error(f"Error in calling get all booking order API with: {e}")

        return response_json, status
