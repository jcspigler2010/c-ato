#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[59]:


class imgRequestError(Exception):
    pass


# In[60]:


def import_poam_template_xlsx(file):

    workbook = load_workbook(filename=file)
    return workbook


# In[61]:


def create_label_dictionary(image):

    try:
        label_dict = {}
        for label in image['labels']:

            label_dict.update({label.split(':')[0]:label.split(':')[1]})
        return label_dict
    except:
        pass


# In[62]:


def control_vulnerability_description(vulnerability):

    return vulnerability['description']


# In[63]:


def office_org(label_dict):
    return return_label(label_dict,'OFFICE_ORG')


# In[64]:


def security_control_number():
    pass


# In[65]:



def return_label(label_dict,target_label):

    try:
        returned_label = label_dict[target_label]
        return returned_label
    except:
        pass


# In[66]:


def security_checks(vulnerability):

    return vulnerability['cve']

    pass


# In[67]:


def resources_required():

    return "eMASS populated"

    pass


# In[68]:


def return_cve_tags(vulnerability,cve_tag):
    cve_tag = parse_vulnTagInfos(vulnerability,cve_tag)
    return cve_tag


# In[69]:


def scheduled_completion_date(vulnerability):
    return parse_vulnTagInfos(vulnerability,"Scheduled Completion Date")


# In[70]:


def milestone_with_completion_dates(vulnerability):
    return parse_vulnTagInfos(vulnerability,"Milestone with Completion Dates")


# In[71]:


def milestone_changes(vulnerability):
    return parse_vulnTagInfos(vulnerability,"Milestone Changes")


# In[72]:


def source_identifying_vulnerability():

    return "Scanned by Prisma Cloud Compute"


# In[73]:


def status(vulnerability):
    return parse_vulnTagInfos(vulnerability,"Status")


# In[74]:


def comments(vulnerability):
    comments = parse_vulnTagInfos(vulnerability,"Comments")
    return comments


# In[75]:


def raw_severity(vulnerability):

    raw_severity = vulnerability['severity']
    return raw_severity


# In[76]:


def devices_affected(image):
    devices_affected = ''
    for tag in image['tags']:
        devices_affected+=tag['registry']+"/"+tag['repo']+":"+tag['tag']
    return devices_affected


# In[94]:


def mitigations_inhouse(vulnerability):
    return return_cve_tags(vulnerability,"Mitigations in-house")


# In[78]:


def predisposing_conditions():
    pass


# In[79]:


def severity():

    return "Moderate"


# In[80]:


def relevance_of_threat():
    pass


# In[81]:


def threat_description():
    pass


# In[82]:


def likelihood():
    pass


# In[83]:


def impact():
    pass


# In[84]:


def impact_description():
    pass


# In[85]:


def residual_risk_level():
    pass


# In[86]:


def recommendations(vulnerability):
    recommendations = vulnerability['link']
    return recommendations


# In[87]:


def resulting_residual_risk_after_proposed_mitigations():
    pass


# In[88]:


def parse_vulnTagInfos(vulnerability,vulnTag):
    try:
        for vulnTagInfo in vulnerability['vulnTagInfos']:
            if vulnTagInfo['name'] == vulnTag:
                return vulnTagInfo['comment']
    except:
            pass


# In[89]:


def create_excel_drop_down():
    dv = DataValidation(type="list", formula1='"Very Low, Low, Moderate, High, Very High"')
    return dv



# In[90]:


def define_cell(column_map,row):
    cell = column_map + str(row)
    return column_map


# In[91]:


def populate_poam_template_xlsx(poam,prisma_json,exported_by):

    row = 8
    sheet = poam.active
    sheet["C2"] = date.today()
    sheet["C3"] = exported_by

    if prisma_json['images']:

        for image in prisma_json['images']:
            label_dict = create_label_dictionary(image)

            for vulnerability in image['vulnerabilities']:

                sheet["C6"] = return_label(label_dict,'DOD_IT_REG_NO')
                sheet["C5"] = return_label(label_dict,'SYSTEM_PROJECT_NAME')
                sheet["J2"] = return_label(label_dict,'SYSTEM_TYPE')
                sheet["J4"] = return_label(label_dict,'POC_NAME')
                sheet["J6"] = return_label(label_dict,'POC_EMAIL')
                sheet["J5"] = return_label(label_dict,'POC_EMAIL')
                sheet["C4"] = return_label(label_dict,'DOD_COMPONENT')

                # office_org
                sheet[office_org_map+str(row)] = office_org(label_dict)

    #             # control_vulnerability_description
                sheet[control_vulnerability_description_map+str(row)] = control_vulnerability_description(vulnerability)

    #             # scheduled_completion_date
                sheet[scheduled_completion_date_map+str(row)] = scheduled_completion_date(vulnerability)

    #             # security_control_number

    #             # security_checks
                sheet[security_checks_map+str(row)] = security_checks(vulnerability)

    #             # resources_required
                sheet[resources_required_map+str(row)] = resources_required()

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
                sheet[mitigations_inhouse_map+str(row)] = mitigations_inhouse(vulnerability)

    #             # predisposing_conditions

    #             # severity
    #             drop down

    #             # relevance_of_threat
                # drop down

    #             # threat_description

    #             # likelihood
                # dropdown

    #             # impact
                # dropdown

    #             # impact_description

    #             # residual_risk_level
                # dropdown


    #             # recommendations
                sheet[recommendations_map+str(row)] = recommendations(vulnerability)

    #             # resulting_residual_risk_after_proposed_mitigations

                row +=1

    return poam


# In[92]:


def output_poam_xlsx(poam,app,build):

    build = str(build)
    today = date.today()
    filename = "POAM-"+app+"-build-"+build+"-"+today.isoformat()+".xlsx"
    print("File output:  "+ filename)
    poam.save(filename=filename)



# In[37]:


def parse_args():
    """
    CLI argument handling
    """

    desc = 'Generate a POAM spreadsheet for hosts, images, CI images and running containers\n'

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
    p.add_argument('-eu','--export_user',metavar='EXPORT_USER',help='User exporting POAM')
    args = p.parse_args()

    # Populate args by env vars if they're set
    envvar_map = {'TL_USER':'user','TL_CONSOLE':'console','TL_PASS':'password','TL_COLLECT':'collection','TL_ID':'entity_id','TL_TARGET':'target','POAM_TEMP':'poam_template','export_user':'EXPORT_USER'}
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
        args.entity_id = raw_input('')
    else:
        arg_errs.append('entity_id (-id, --entity_id)')

    if getattr(args,'target',None) is None:
        args.target = raw_input('')
    else:
        arg_errs.append('target (-t, --target)')

    if getattr(args,'poam_template',None) is None:
        args.poam_template = raw_input('')
    else:
        arg_errs.append('poam_template (-m, --poam_template)')

    if getattr(args,'export_user',None) is None:
        args.export_user = raw_input('Please enter user name who is exporting the POAM: ')
    else:
        arg_errs.append('export_user (-eu, --export_user)')

    return args


# In[97]:


def get_prisma_data_json(console,user,password,collection,target,entity_id):
    json_return = {}
    json_count = 0
    for t in target.split(','):
        api_endpt = '/api/v1/'+t+'?id='+entity_id+'&&collections='+collection
        print("Retrieving data on: " + api_endpt)
        request_url = console + api_endpt
        image_req=requests.get(request_url, auth=HTTPBasicAuth(user,password), verify=False)
        json_return[t] = image_req.json()
        if image_req.status_code != 200:
            raise imgRequestError('GET /api/v1/'+target+' {} {}'.format(image_req.status_code,image_req.reason))

    return json_return


# In[1]:


def main():
    urllib3.disable_warnings()
    args = parse_args()

    try:
        prisma_json = get_prisma_data_json(args.console,args.user,args.password,args.collection,args.target,args.entity_id)
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
        new_poam = populate_poam_template_xlsx(poam,prisma_json,args.export_user)
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
