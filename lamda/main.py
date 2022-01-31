import os
import json

def handler(event,context): 
  session_policy = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowStatement1",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::*"
            ]
        },
        {
            "Sid": "AllowCreationOfFolder",
            "Action": [
                "s3:PutObject"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::${transfer:HomeBucket}/*"
            ]
        },
        {
            "Sid": "AllowListingOfUserFolder",
            "Action": [
                "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::${transfer:HomeBucket}"
            ],
            "Condition": {
                "StringEquals": {
                    "s3:prefix": [
                        "",
                        "${transfer:HomeFolder}"
                    ]
                }
            }
        },
        {
            "Sid": "AllowStatement3",
            "Action": [
                "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::${transfer:HomeBucket}"
            ],
            "Condition": {
                "StringLike": {
                    "s3:prefix": [
                        "${transfer:HomeFolder}/*"
                    ]
                }
            }
        },
        {
            "Sid": "HomeDirObjectAccess",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:DeleteObjectVersion",
                "s3:GetObjectVersion",
                "s3:GetObjectACL",
                "s3:PutObjectACL"
            ],
            "Resource": [
                "arn:aws:s3:::${transfer:HomeDirectory}*"
            ]
        }
    ]
}"""
  
  json_string = """ {
   "id": 5539,
   "uuid": "195ff34b-4e3a-4b9d-b80e-7a1221be1941",
   "email": "jhall@opengov.com",
   "first_name": "Jeremiah",
   "last_name": "Hall",
   "full_name": "Jeremiah Hall",
   "role": {
       "name": "opengov_engineer",
       "display_name": "OpenGov Engineer"
   },
   "abilities": {
       "entity": {
           "create": false,
           "destroy": false,
           "update": false,
           "read_all": true,
           "switch_to": true
       },
       "report": {
           "create": false,
           "destroy": false,
           "update": false,
           "read_all": true
       },
       "saved_view": {
           "create": false,
           "destroy": false,
           "update": false,
           "read_all": true
       },
       "data_manager/coa_mask": {
           "create": false,
           "destroy": false,
           "update": false,
           "read_all": true
       },
       "feedback": {
           "create": true,
           "destroy": false,
           "update": false,
           "forward": false,
           "read_all": true
       },
       "budgeting/budget": {
           "create": false,
           "destroy": false,
           "update": false,
           "read_all": true
       },
       "budgeting/budget_invite": {
           "create": false,
           "destroy": false,
           "update": false,
           "read_all": true
       },
       "feature_license_agreement": {
           "create": false,
           "destroy": false,
           "update": false,
           "read_all": true
       },
       "user": {
           "create": false,
           "destroy": false,
           "update": true,
           "read_all": true,
           "promote": true
       },
       "api_key": {
           "create": true,
           "destroy": true,
           "update": true,
           "read_all": true,
           "manage": true
       }
   },
   "demote_at": null,
   "disabled": false,
   "environment": "integration",
   "avatar": null,
   "control_panel_menu_items": [
       {
           "id": "network",
           "name": "Network",
           "location_template": "//controlpanel.ogintegration.us/network/${entity}",
           "icon": "network",
           "requires_entity": false,
           "version": null,
           "requires_feature_permission": null
       },
       {
           "id": "reports",
           "name": "Reports",
           "location_template": "//controlpanel.ogintegration.us/reports#${entity}",
           "icon": "reports",
           "requires_entity": true,
           "version": null,
           "requires_feature_permission": null
       },
       {
           "id": "budgets",
           "name": "Budgets",
           "location_template": "//controlpanel.ogintegration.us/budgets/${entity}",
           "icon": "budgets",
           "requires_entity": true,
           "version": null,
           "requires_feature_permission": "budgets"
       },
       {
           "id": "data",
           "name": "Data",
           "location_template": "//controlpanel.ogintegration.us/data_manager/${entity}",
           "icon": "data",
           "requires_entity": true,
           "version": null,
           "requires_feature_permission": null
       },
       {
           "id": "portal",
           "name": "Portal",
           "location_template": "//controlpanel.ogintegration.us/portal/${entity}/visitor_analytics",
           "icon": "portal",
           "requires_entity": false,
           "version": null,
           "requires_feature_permission": null
       },
       {
           "id": "initiatives",
           "name": "Initiatives",
           "location_template": "//controlpanel.ogintegration.us/strategic-initiatives/${entity}",
           "icon": "initiatives",
           "requires_entity": true,
           "version": null,
           "requires_feature_permission": "strategic_initiatives"
       },
       {
           "id": "stories",
           "name": "Stories",
           "location_template": "//controlpanel.ogintegration.us/stories/${entity}",
           "icon": "stories",
           "requires_entity": true,
           "version": null,
           "requires_feature_permission": "stories"
       },
       {
           "id": "manage",
           "name": "Settings",
           "location_template": "//controlpanel.ogintegration.us/controlpanel#${entity}/manage",
           "icon": "manage",
           "requires_entity": false,
           "version": null,
           "requires_feature_permission": null
       }
   ],
   "user_intercom_hash": "ea301e2c848e581fa5e6d9dafd487ee9cb733fbf571e8090debb91145ac1d082",
   "groups": [
       "opengov"
   ],
   "title": "",
   "department": "",
   "last_seen": "2022-01-18T10:23:57.531-08:00",
   "created_at": "2016-03-10T14:24:37.681-08:00",
   "entity": {
       "id": "controlpanel",
       "uuid": "0bb44e35-83a2-4101-bab2-85dc2e4d2dea",
       "name": "Control Panel ",
       "display_name": "OpenGov",
       "country": "US",
       "state": "CA",
       "address": "Mountain View, CA12345",
       "entity_type": {
           "name": "Borough",
           "value": "borough"
       },
       "subdomain": "controlpanel",
       "custom_domain": null,
       "homepage_url": "http://www.opengov.com",
       "logo": "https://s3.amazonaws.com/delphius-integration-2/entities/logos/000/000/015/header_image/data.png?1452573881",
       "entity_id": 17,
       "default_coa_id": "c981247f-dfbf-4b28-bed0-cfb0c4813430",
       "color": {
           "color": "#bf3f3f",
           "index": 0
       },
       "fiscal_year_start_month": 7,
       "population": null,
       "fiscal_year_start_date_formatted": "July 01",
       "default_report_id": null,
       "budget_101": true,
       "feature_permissions": [
           "budget_fund_balance_projection",
           "data_manager",
           "unified_data",
           "engineering_only_budget_etag_validation",
           "budgets",
           "fund_balance_import",
           "workforce_summary_reporting",
           "date_based_budget",
           "engineering_only_optimize_account_string_import",
           "engineering_only_upload_eventing",
           "strategic_initiatives",
           "enable_strict_transaction_date_validation",
           "multiple_amount_columns",
           "stories"
       ],
       "report_preferences": {
           "expenses_variance_formula": "actual_minus_budget",
           "revenues_variance_formula": "actual_minus_budget"
       },
       "active": true,
       "published": false,
       "emblem": null,
       "transparency_url": "https://controlpanel.ogintegration.us/",
       "tos_url": "",
       "accepted_budget_license_agreement": true,
       "created_at": "2013-06-18T15:27:42.000-07:00",
       "updated_at": "2021-12-22T05:07:39.296-08:00",
       "longitude": null,
       "latitude": null,
       "salesforce_id": "",
       "abilities": {
           "update": false,
           "unpublish": false,
           "upload_logo": false,
           "manage": false,
           "switch_to": true
       },
       "documents": []
    }
  }
  """
  user_info = json.loads(json_string)
  bucket_name = '/myteststacksftp'
  print(user_info['entity']['entity_id'], user_info['first_name'])
  allowed_users = [
     {'username' : user_info['first_name'], 'password' : "MySuperSecretPassword", 'HomeDirectory' : bucket_name + '/' + str(user_info['entity']['entity_id'])},
     {'username' : "myuser2", 'password' : "MySuperSecretPassword", 'HomeDirectory' : "/myteststacksftp/user2"}
  ]
  
  iam_user = next(user for user in allowed_users if user['username'] == event['username'])
  iam_role = "arn:aws:iam::918073871806:role/myteststack"
  
  if (event['password'] == '' and (event['protocol'] == 'FTP' or event['protocol'] == 'FTPS')):
     #Return HTTP status 200 but with no role in the response to indicate authentication failure
     response = {}
  elif (event['serverId'] != '' and iam_user):
     response = {
      'Role': iam_role, #The user will be authenticated if and only if the Role field is not blank
      'Policy': session_policy, #Optional JSON blob to further restrict this user's permissions
      'HomeDirectory': iam_user['HomeDirectory'] #Not required, defaults to '/'
     }
     #Check if password is provided
     if (event['password'] == ''):
      #If no password provided, return the user's SSH public key
      response['PublicKeys'] = [ "ssh-rsa myrsapubkey" ]
     #Check if password is correct
     elif (event['password'] != iam_user['password']):
      #Return HTTP status 200 but with no role in the response to indicate authentication failure
      response = {}
  else:
     #Return HTTP status 200 but with no role in the response to indicate authentication failure
     response = {}
  return response