import json
import requests


def get_parameter_value(parameters, name):
    for param in parameters:
        if param['name'] == name:
            return param['value']
    return None


def lambda_handler(event, context):
    print("event: {}".format(event))
    agent = event.get('agent')
    function = event.get('function')
    actionGroup = event.get('actionGroup')
    parameters = event.get('parameters', [])

    # Base URL for FastAPI application
    base_url = "https://7133-103-211-17-154.ngrok-free.app"  # Update with your FastAPI application URL

    # Make API request to apply leave
    try:
        response_message = ''

        if function.replace("-", "_") == "apply_leave":

            # Extract parameters from the list
            email_id = get_parameter_value(parameters, 'email_id')
            start_date = get_parameter_value(parameters, 'start_date')
            end_date = get_parameter_value(parameters, 'end_date')
            apply_leave_url = f"{base_url}/apply-leave/"

            response = requests.post(apply_leave_url, json={
                "email_id": email_id,
                "start_date": start_date,
                "end_date": end_date,
                "leave_type": "sick_leave"
            })

            response_data = response.json()

            if response.status_code == 200:
                response_message = f"Leave applied successfully: {response_data}"
            else:
                response_message = f"Failed to apply leave: {response_data.get('detail', 'Unknown error')}"

        elif function.replace("-", "_") == "check_leave_balance":
            email_id = get_parameter_value(parameters, 'email_id')
            check_leave_url = f"{base_url}/leave-balance/"

            response = requests.get(check_leave_url, params={
                "email_id": email_id
            })

            response_data = response.json()

            if response.status_code == 200:
                response_message = f"Category wise balance leave: {response_data}"
            else:
                response_message = f"Unable to fetch leave balance: {response_data.get('detail', 'Unknown error')}"

    except Exception as e:
        response_message = f"Unable to do the action: {str(e)}"

    # Prepare the response
    responseBody = {
        "TEXT": {
            "body": response_message
        }
    }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }
    }

    lambda_response = {
        'response': action_response,
        'messageVersion': event.get('messageVersion', '1.0')
    }

    print("Response: {}".format(lambda_response))

    return lambda_response
