#!/usr/bin/env python
# coding: utf-8


import datetime
from dataclasses import dataclass

@dataclass
class PoamHeaders:
  control_vulnerability_description: str
  security_control_number: str
  office_org: str
  security_checks: str
  resources_required: str
  scheduled_completion_date: str
  milestone_with_completion_dates: str
  milestone_changes: str
  source_identifying_vulnerability: str
  status: str
  comments: str
  raw_severity: str
  devices_affected: str
  mitigations_inhouse: str
  predisposing_conditions: str
  severity: str
  relevance_of_threat: str
  threat_description: str
  likelihood: str
  impact: str
  impact_description: str
  residual_risk_level: str
  recommendations: str
  resulting_residual_risk_after_proposed_mitigations: str





