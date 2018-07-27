from django.db import models
from django.conf import settings
from django.utils.text import slugify


# model.FileField(uploadto=proof_of_agency_status_uh)
def proof_of_agency_status_uh(instance, filename):
    return '{}/proof_of_agency_status/{}'.format(slugify(instance.name), filename)


# model.FileField(scan_990)
def scan_990_uh(instance, filename):
    return '{}/scan_990_uh/{}'.format(slugify(instance.name), filename)

"""
h2 Agency Information
         :name
         :distributor_type, collection: %w[Agency Hospital], as: :radio_buttons
         :agency_type, collection: ['501(c)3', 'Religious Organization', 'Government Organization']
         :proof_of_agency_status, as: :file
        ul
          li 501(c)3 Letter
          li Letter of Good Standing from Denominational Headquarters
          li Government Letterhead
         :agency_mission, as: :text
         :address1
         :address2
         :city
         :state, collection: states
         :zip_code

        h2 Media Information
         :website
         :facebook
         :twitter

        h2 Agency Stability
         :founded, as: :integer, input_html: { min: 1800, max: Date.current.year }
         :form_990, as: :radio_buttons
         :scan_990, as: :file
         :program_name
         :program_description
         :program_age
         :case_management, as: :radio_buttons
         :evidence_based, as: :radio_buttons
         :evidence_based_description, as: :text
         :program_client_improvement, as: :text
         :diaper_use, collection: diaper_use, as: :check_boxes
         :other_diaper_use
         :currently_provide_diapers, as: :radio_buttons
         :turn_away_child_care, as: :radio_buttons

        h3 Program Address
         :program_address1
         :program_address2
         :program_city
         :program_state, collection: states
         :program_zip_code

        h2 Organizational Capacity
         :max_serve
         :incorporate_plan, as: :text
         :responsible_staff_position, as: :radio_buttons
         :storage_space, as: :radio_buttons
         :describe_storage_space, as: :text
         :trusted_pickup, as: :radio_buttons

        h2 Population Served
         :income_requirement_desc, as: :radio_buttons
         :serve_income_circumstances, as: :radio_buttons
         :income_verification, as: :radio_buttons
         :internal_db, as: :radio_buttons
         :maac, as: :radio_buttons

        h3 Ethnic composition of those served
         :population_black, input_html: { min: 0, max: 100 }
         :population_white, input_html: { min: 0, max: 100 }
         :population_hispanic, input_html: { min: 0, max: 100 }
         :population_asian, input_html: { min: 0, max: 100 }
         :population_american_indian, input_html: { min: 0, max: 100 }
         :population_island, input_html: { min: 0, max: 100 }
         :population_multi_racial, input_html: { min: 0, max: 100 }
         :population_other, input_html: { min: 0, max: 100 }

        h3 Zips served
         :zips_served

        h3 Poverty information of those served
         :at_fpl_or_below, input_html: { min: 0, max: 100 }
         :above_1_2_times_fpl, input_html: { min: 0, max: 100 }
         :greater_2_times_fpl, input_html: { min: 0, max: 100 }
         :poverty_unknown, input_html: { min: 0, max: 100 }

        h3 Ages served
         :ages_served

        h2 Executive Director
         :executive_director_name
         :executive_director_phone
         :executive_director_email

        h2 Program Contact Person
         :program_contact_name
         :program_contact_phone
         :program_contact_mobile
         :program_contact_email

        h2 Diaper Pick Up Person
         :pick_up_method, collection: %w[volunteers staff courier]
         :pick_up_name
         :pick_up_phone
         :pick_up_email

        h2 Agency Distribution Information
         :distribution_times
         :new_client_times
         :more_docs_required

        h2 Sources of Funding
         :sources_of_funding, collection: funding_sources, as: :check_boxes
         :sources_of_diapers, collection: diaper_sources, as: :check_boxes
         :diaper_budget, collection: %w[N/A Yes No], as: :radio_buttons
         :diaper_funding_source, collection: %w[N/A Yes No], as: :radio_buttons



Collections:
    DIAPER_USE = [
   'Emergency supplies for families (off site)',
   'Homeless shelter',
   'Domestic violence shelter',
   'On-site residential program',
   'Outreach',
   'Alcohol/Drug Recovery',
   'Daycare',
   'Foster Care',
   'Other'
  ]

  FUNDING_SOURCES = [
    'Grants - Foundation',
    'Grants - State',
    'Grants - Federal',
    'Corporate Donations',
    'Individual Donations',
    'Other'
  ]

  DIAPER_SOURCES = [
    'Purchase Retail',
    'Purchase Wholesale',
    'Diaper Drives',
    'Diaper Drives conducted by others',
    'Other'
  ]
"""

class Partner(models.Model):

    AGENCY_DISTRIBUTOR_TYPES = settings.ACENCY_DISTRIBUTOR_TYPES

    name = models.CharField(max_length=2048, null=False, blank=False)
    distributor_type = models.CharField(max_length=2,
                                        choices=PARTNER_DISTRIBUTOR_TYPES)
    agency_types = models.ChoiceField(max_length=2,
                                      choices=PARTNER_AGENCY_TYPES)
    proof_of_agency_status = model.FileField() #  TODO: add file arguments
