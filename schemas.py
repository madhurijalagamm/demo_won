from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal
class ProposalBase(BaseModel):
    ods_2_day__c: Optional[bool] = None
    ods_2_day_max_quantity__c: Optional[int] = None
    ods_3_day__c: Optional[bool] = None
    ods_3_day_max_quantity__c: Optional[int] = None
    ods_5_day__c: Optional[bool] = None
    ods_5_day_max_quantity__c: Optional[int] = None
    ods_account__c: Optional[str] = None
    ods_accounting__c: Optional[str] = None
    ods_additional_attributes_notes__c: Optional[str] = None
    ods_buyout__c: Optional[bool] = None
    ods_consider_for_revenue_generation__c: Optional[bool] = None
    ods_certified_mail__c: Optional[bool] = None
    ods_commission_percent__c: Optional[Decimal] = None
    ods_complex_quote__c: Optional[bool] = None
    ods_expected_end_date__c: Optional[date] = None
    ods_expected_start_date__c: Optional[date] = None
    ods_csm__c: Optional[str] = None
    ods_customer_requirements__c: Optional[str] = None
    ods_data_composition__c: Optional[str] = None
    ods_data_composition_other__c: Optional[str] = None
    ods_delivery_to_post_office__c: Optional[bool] = None
    ods_description__c: Optional[str] = None
    ods_distribution__c: Optional[str] = None
    ods_distribution_other__c: Optional[str] = None
    ods_due_date__c: Optional[date] = None
    ods_estimated_quote_value__c: Optional[Decimal] = None
    ods_estimation_leader__c: Optional[str] = None
    ods_estimation_checklist__c: Optional[str] = None
    ods_estimating_team_user__c: Optional[str] = None
    ods_file_available_for_asset_creation__c: Optional[bool] = None
    ods_first_class_mail__c: Optional[bool] = None
    ods_fulfillment__c: Optional[str] = None
    ods_is_duplicate_proposal__c: Optional[bool] = None
    ods_is_enddate_blank__c: Optional[bool] = None
    cpq_it_required__c: Optional[bool] = None
    ods_jira_number__c: Optional[str] = None
    ods_jira_number_formula__c: Optional[str] = None
    ods_legacy_proposal_id__c: Optional[str] = None
    ods_maximum_qty__c: Optional[Decimal] = None
    ods_next_day__c: Optional[bool] = None
    ods_next_day_max_quantity__c: Optional[int] = None
    ods_opportunity__c: Optional[str] = None
    ods_packaging__c: Optional[str] = None
    ods_packaging_other__c: Optional[str] = None
    ods_pending_activation__c: Optional[bool] = None
    ods_plant__c: Optional[str] = None
    ods_po_box_collection__c: Optional[bool] = None
    ods_presented_date__c: Optional[date] = None
    ods_previous_legacy_proposal_id__c: Optional[str] = None
    ods_previous_proposal_id__c: Optional[str] = None
    ods_pricing_notes__c: Optional[str] = None
    ods_primary_contact__c: Optional[str] = None
    ods_project_owner_project_contact__c: Optional[str] = None
    ods_proposal_generated_date__c: Optional[date] = None
    ods_proposal_id__c: Optional[str] = None
    ods_proposal_name__c: Optional[str] = None
    ods_proposal_primary__c: Optional[bool] = None
    ods_quote_stage__c: Optional[str] = None
    ods_ready_for_estimation_date__c: Optional[date] = None
    ods_ready_for_sales_date__c: Optional[date] = None
    ods_sales_rep__c: Optional[str] = None
    ods_same_day__c: Optional[bool] = None
    ods_same_day_max_quantity__c: Optional[int] = None
    ods_schedule__c: Optional[str] = None
    ods_scope_of_work__c: Optional[str] = None
    ods_secure_destruction__c: Optional[bool] = None
    ods_standard_mail__c: Optional[bool] = None
    ods_submitted_by__c: Optional[str] = None
    ods_t_c__c: Optional[str] = None
    ods_total_net_price__c: Optional[Decimal] = None
    ods_valid_until_date__c: Optional[date] = None

class ProposalCreate(ProposalBase):
    pass

class ProposalUpdate(ProposalBase):
    pass

class Proposal(ProposalBase):
    id: str
    class Config:
        from_attributes = True
