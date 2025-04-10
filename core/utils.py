import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

def create_email_campaign(api_key, campaign_name, subject, sender_name, sender_email, html_content, list_ids, scheduled_time):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = api_key

    api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
    email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
        name=campaign_name,
        subject=subject,
        sender={"name": sender_name, "email": sender_email},
        type="classic",
        html_content=html_content,
        recipients={"listIds": list_ids},
        scheduled_at=scheduled_time
    )
    try:
        api_response = api_instance.create_email_campaign(email_campaigns)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling EmailCampaignsApi->create_email_campaign: {e}\n")
    except ApiException as e:
        print(f"An error occurred: {e}")