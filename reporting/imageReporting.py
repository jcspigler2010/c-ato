#!/usr/bin/env python
# coding: utf-8
## e.g. python imageReporting.py -c https://twistlock-console.oceast.cloudmegalodon.us -u jonathan@clearshark.com -p {password} -o All -id sha256:c87e9a853fe046f445a1250c62432127db8b8b79e24ce73d68f6e74f86f147ac -t images -m POAM_Export_Sample.xlsx
# In[51]:


#!/usr/bin/env python
import time
from datetime import datetime
import sys
import getpass
import argparse
import json
import os
import requests
from requests.auth import HTTPBasicAuth
from jinja2 import Template
import urllib3
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
import json
from  datetime  import date
from mapping import  control_vulnerability_description_map, security_control_number_map, office_org_map, security_checks_map, resources_required_map, scheduled_completion_date_map, milestone_with_completion_dates_map, milestone_changes_map, source_identifying_vulnerability_map, status_map, comments_map, raw_severity_map, devices_affected_map, mitigations_inhouse_map, predisposing_conditions_map, severity_map, relevance_of_threat_map, threat_description_map, likelihood_map, impact_map, impact_description_map, residual_risk_level_map, recommendations_map, resulting_residual_risk_after_proposed_mitigations_map


# In[4]:


class imgRequestError(Exception):
    pass


# In[5]:


def import_poam_template_xlsx(file):

    workbook = load_workbook(filename=file)
    return workbook


# In[6]:


def create_label_dictionary(image):

    try:
        label_dict = {}
        for label in image['labels']:

            label_dict.update({label.split(':')[0]:label.split(':')[1]})
            return label_dict
    except:
        pass


# In[7]:


def control_vulnerability_description(vulnerability):

    description = vulnerability['description']
    return  description


# In[8]:


def security_control_number():
    pass


# In[9]:



def return_label(label_dict,target_label):

    try:
        returned_label = label_dict[target_label]
        return returned_label
    except:
        pass


# In[10]:


def security_checks(vulnerability):

    security_check = vulnerability['cve']
    return security_check

    pass


# In[11]:


def resources_required():

    return "eMASS populated"

    pass


# In[12]:


def scheduled_completion_date(vulnerability):
    schedule_completion_date = parse_vulnTagInfos(vulnerability,"Scheduled Completion Date")
    return schedule_completion_date


# In[13]:


def milestone_with_completion_dates(vulnerability):
    schedule_completion_date = parse_vulnTagInfos(vulnerability,"Milestone with Completion Dates")
    return schedule_completion_date


# In[14]:


def milestone_changes(vulnerability):
    milestone_changes = parse_vulnTagInfos(vulnerability,"Milestone Changes")
    return milestone_changes


# In[15]:


def source_identifying_vulnerability():

    return "Scanned by Prisma Cloud Compute"


# In[16]:


def status(vulnerability):
    status = parse_vulnTagInfos(vulnerability,"Status")
    return status


# In[17]:


def comments(vulnerability):
    comments = parse_vulnTagInfos(vulnerability,"Comments")
    return comments


# In[18]:


def raw_severity(vulnerability):

    raw_severity = vulnerability['severity']
    return raw_severity


# In[19]:


def devices_affected(image):
    devices_affected = ''
    for tag in image['tags']:
        devices_affected+=tag['registry']+"/"+tag['repo']+":"+tag['tag']
    return devices_affected


# In[20]:


def mitigations_inhouse():
    pass


# In[21]:


def predisposing_conditions():
    pass


# In[22]:


def severity():

    return "Moderate"


# In[23]:


def relevance_of_threat():
    pass


# In[24]:


def threat_description():
    pass


# In[25]:


def likelihood():
    pass


# In[26]:


def impact():
    pass


# In[27]:


def impact_description():
    pass


# In[28]:


def residual_risk_level():
    pass


# In[29]:


def recommendations(vulnerability):
    recommendations = vulnerability['link']
    return recommendations


# In[30]:


def resulting_residual_risk_after_proposed_mitigations():
    pass


# In[31]:


def parse_vulnTagInfos(vulnerability,vulnTag):
    try:
        for vulnTagInfo in vulnerability['vulnTagInfos']:
            if vulnTagInfo['name'] == vulnTag:
                return vulnTagInfo['comment']
    except:
            pass


# In[32]:


def create_excel_drop_down():
    dv = DataValidation(type="list", formula1='"Very Low, Low, Moderate, High, Very High"')
    return dv



# In[33]:


def define_cell(column_map,row):
    cell = column_map + str(row)
    return column_map


# In[34]:


def populate_poam_template_xlsx(poam,images):

    row = 8
    sheet = poam.active

    for image in images:
        label_dict = create_label_dictionary(image)

        for vulnerability in image['vulnerabilities']:

            # office_org
            sheet[office_org_map+str(row)] = return_label(label_dict,'OFFICE_ORG')

#             # control_vulnerability_description
            sheet[control_vulnerability_description_map+str(row)] = control_vulnerability_description(vulnerability)

#             # scheduled_completion_date
            sheet[scheduled_completion_date_map+str(row)] = scheduled_completion_date(vulnerability)

#             # security_control_number

#             # security_checks
            sheet[security_checks_map+str(row)] = security_checks(vulnerability)

#             # resources_required

#             # milestone_with_completion_dates
            sheet[milestone_with_completion_dates_map+str(row)] = milestone_with_completion_dates(vulnerability)

#             # milestone_changes
            sheet[milestone_changes_map+str(row)] = milestone_changes(vulnerability)

#             # source_identifying_vulnerability
            sheet[source_identifying_vulnerability_map+str(row)] = source_identifying_vulnerability()

#             # status
            sheet[status_map+str(row)] = status(vulnerability)

#             # comments
            sheet[comments_map+str(row)] = comments(vulnerability)

#             # raw_severity
            sheet[raw_severity_map+str(row)] = raw_severity(vulnerability)

#             # devices_affected
            sheet[devices_affected_map+str(row)] = devices_affected(image)

#             # mitigations_inhouse

#             # predisposing_conditions

#             # severity

#             # relevance_of_threat

#             # threat_description

#             # likelihood

#             # impact

#             # impact_description

#             # residual_risk_level

#             # recommendations
            sheet[recommendations_map+str(row)] = recommendations(vulnerability)

#             # resulting_residual_risk_after_proposed_mitigations

            row +=1


    date_exported = date.today()
    exported_by = ""
    dod_component = return_label(label_dict,'DOD_IT_REG_NO')
    system_project_name = return_label(label_dict,'SYSTEM_PROJECT_NAME')
    system_type = return_label(label_dict,'SYSTEM_TYPE')
    poc_name = return_label(label_dict,'POC_NAME')
    poc_email = return_label(label_dict,'POC_EMAIL')
    dod_component = return_label(label_dict,'DOD_COMPONENT')


    return poam


# In[35]:


def output_poam_xlsx(poam,app,build):

    build = str(build)
    today = date.today()
    filename = "POAM-"+app+"-build-"+build+"-"+today.isoformat()+".xlsx"
    print("File output:  "+ filename)
    poam.save(filename=filename)


# In[54]:


def parse_args():
    """
    CLI argument handling
    """

    desc = 'Generate an HTML report of CVEs per image, displaying the data to STDOUT\n'

    epilog = 'The console and user arguments can be supplied using the environment variables TL_CONSOLE and TL_USER.'
    epilog += ' The password can be passed using the environment variable TL_PASS.'
    epilog += ' The user will be prompted for the password when the TL_PASS variable is not set.'
    epilog += ' Environment variables override CLI arguments.'

    p = argparse.ArgumentParser(description=desc,epilog=epilog)
    p.add_argument('-c','--console',metavar='TL_CONSOLE', help='query the API of this Console')
    p.add_argument('-u','--user',metavar='TL_USER',help='Console username')
    p.add_argument('-p','--password',metavar='TL_PASS',help='Console user password')
    p.add_argument('-d','--debug',help='Provide a debug console dump of HTML report',action='store_true')
    p.add_argument('-o','--collection',metavar='TL_COLLECT',help='Prisma cloud compute colllections to filter results')
    p.add_argument('-id','--entity_id',metavar='TL_ID',help='Filter collection to specific image or host ID')
    p.add_argument('-t','--target',metavar='TL_TARGET',help='Targeted entity type to generate report on (e.g. container image, host, running containers) Options running_container,image,host ')
    p.add_argument('-m','--poam_template',metavar='POAM_TEMP',help='specify xlsx POAM template')
    args = p.parse_args()

    # Populate args by env vars if they're set
    envvar_map = {'TL_USER':'user','TL_CONSOLE':'console','TL_PASS':'password','TL_COLLECT':'collection','TL_ID':'entity_id','TL_TARGET':'target','POAM_TEMP':'poam_template'}
    for evar in envvar_map.keys():
        evar_val = os.environ.get(evar,None)
        if evar_val is not None:
            setattr(args,envvar_map[evar],evar_val)

    arg_errs = []
    if len(arg_errs) > 0:
        err_msg = 'Missing argument(s): {}'.format(', '.join(arg_errs))
        p.error(err_msg)

    if getattr(args,'console',None) is None:
        args.console = raw_input('Enter console url: ')
    else:
        arg_errs.append('console (-c,--console)')
    if getattr(args,'user',None) is None:
        args.user = raw_input('Enter username: ')
    else:
        arg_errs.append('user (-u,--user)')

    if getattr(args,'password',None) is None:
        args.password = getpass.getpass('Enter password: ')
    else:
        arg_errs.append('password (-p, --password)')

    if getattr(args,'collection',None) is None:
        args.collection = raw_input('')
    else:
        arg_errs.append('collection (-o, --collection)')

    if getattr(args,'entity_id',None) is None:
        args.collection = raw_input('')
    else:
        arg_errs.append('entity_id (-id, --entity_id)')

    if getattr(args,'target',None) is None:
        args.collection = raw_input('')
    else:
        arg_errs.append('target (-t, --target)')

    if getattr(args,'poam_template',None) is None:
        args.collection = raw_input('')
    else:
        arg_errs.append('poam_template (-m, --poam_template)')

    return args


# In[52]:


def get_prisma_data_json(console,user,password,collection,target,entity_id):
    api_endpt = '/api/v1/'+target+'?id='+entity_id+'&&collections='+collection
    print("Retrieving data on: " + api_endpt)
    request_url = console + api_endpt
    image_req = requests.get(request_url, auth=HTTPBasicAuth(user,password), verify=False)
    if image_req.status_code != 200:
        # This means something went wrong.
        raise imgRequestError('GET /api/v1/'+target+' {} {}'.format(image_req.status_code,image_req.reason))
    return image_req.json()


# In[55]:


def main():
    urllib3.disable_warnings()
    args = parse_args()

    try:
        images_json = get_prisma_data_json(args.console,args.user,args.password,args.collection,args.target,args.entity_id)
    except imgRequestError as e:
        print("Error querying API: {}".format(e))
        return 3

        #Import POAM template specified in args
    try:
        poam = import_poam_template_xlsx(args.poam_template)
        sheet = poam.active
    except imgReqestError as e:
        print("Error importing template: {}".format(e))


    try:
        new_poam = populate_poam_template_xlsx(poam,images_json)
    except imgReqestError as e:
        print("Error creating poam: {}".format(e))

    try:
        output_poam_xlsx(new_poam,"mysite-ruby",1)
    except imgReqestError as e:
        print("Error saving poam: {}".format(e))

    return 0


# In[56]:


if __name__ == '__main__':
    sys.exit(main())


# In[ ]:
